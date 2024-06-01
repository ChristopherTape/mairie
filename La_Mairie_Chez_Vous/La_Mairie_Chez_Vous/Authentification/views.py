from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
# from .models import Agent
from django.contrib.auth.hashers import check_password
from .forms import PasswordResetForm
from Authentification.models import CustomUser
import logging
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)
User = get_user_model()


def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        confirmation_mot_de_passe = request.POST.get('confirmation_mot_de_passe')

        if mot_de_passe != confirmation_mot_de_passe:
            return HttpResponse("Votre mot de passe et votre mot de passe de confirmation ne sont pas identiques !!")
        elif CustomUser.objects.filter(username=username).exists():
            # Vérifiez si un utilisateur avec le même nom existe déjà
            messages.error(request, "le Nom d'utilisateur a deja été utiliser")
        else:
            user = CustomUser.objects.create_user(username=username, first_name=nom, password=mot_de_passe, email=email)
            return redirect('page_accueil')  # Rediriger vers la page après inscription

    return render(request, 'Authentification/inscription.html')


def connexion(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        mot_de_passe = request.POST.get('mot_de_passe')

        if nom and mot_de_passe:
            # Essayer d'authentifier l'utilisateur avec le modèle User de Django
            utilisateur = authenticate(request, username=nom, password=mot_de_passe)
            if utilisateur is not None:
                login(request, utilisateur)
                if utilisateur.is_agent:
                    return redirect('dash_admin')
                else:
                    return redirect('Commander/')  # Redirection vers la page après connexion

            # Si l'authentification échoue pour le modèle User
            messages.error(request, "Le nom d'utilisateur ou le mot de passe est incorrect.")
        else:
            messages.error(request, "Veuillez remplir tous les champs du formulaire.")

    return render(request, 'Authentification/Connexion.html')


def send_email_with_html_body(
        subjet: str, receivers: list, template: str, context: dict
):
    """This fonction help to send a customize email to a specific user or set of users."""
    try:
        message = render_to_string(template, context)

        send_mail(
            subjet,
            message,
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=True,
            html_message=message,
        )
        return True


    except Exception as e:
        logger.error(e)
    return False


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["email"]
            user = User.objects.get(email=data)

            mail_subject = "Réinitialisation de votre mot de passe"
            template = "Authentification/mot_de_passe_oub.html"
            context = {"user": user, "date": datetime.today().date}

            receivers = [data]
            # message = f'bonjour {user.first_name} connectez vous avec ce mot de passe { mdp }  et en suite rendez-vous sur votre tableau de bord pour definir un nouveau mot de passe'
            send_email_with_html_body(
                subjet=mail_subject,
                receivers=receivers,
                template=template,
                context=context,
            )

            return redirect("notif")
    else:
        form = PasswordResetForm()
    return render(request, "Authentification/new_mot_de_passe.html", {"form": form})


def notif(request):
    return render(request, "Authentification/page_null.html")


def change_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)

        user.set_password(password)
        user.save()
        messages.success(request, "Mot de passe changé avec succès.")
        return redirect(
            "connexion"
        )  # Redirigez vers une autre page comme un profil

    return render(request, "Authentification/changer_mdp.html")

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib import messages
from Authentification.models import Agent
from .forms import FormulaireDemandeActeNaissanceForm
from .models import FormulaireDemandeActeNaissance, Transaction
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest

from Authentification.models import CustomUser
from django.template import TemplateDoesNotExist
from django.http import HttpResponse
import json



@login_required
def Commander(request):
    user = request.user
    if not hasattr(user, 'agent'):
        display_name = user.first_name + " " + user.username
    else:
        display_name = user.username
    return render(request, "CommanderDoc/Commander.html", {"user": user, "display_name": display_name})


 
@login_required     
def formulaire2(request):
    mairies = Agent.objects.all()
    if request.method == 'POST':
        request.session['form_data'] = request.POST
        request.session['form_type'] = 'formulaire2'
        return redirect('summary')
    return render(request, "CommanderDoc/formulaire2.html", {'mairies': mairies})

@login_required     
def formulaire3(request):
    mairies = Agent.objects.all()
    if request.method == 'POST':
        request.session['form_data'] = request.POST
        request.session['form_type'] = 'formulaire3'
        return redirect('summary2')
    return render(request, "CommanderDoc/formulaire3.html", {'mairies': mairies})

@login_required     
def formulaire4(request):
    mairies = Agent.objects.all()
    if request.method == 'POST':
        request.session['form_data'] = request.POST
        request.session['form_type'] = 'formulaire4'
        return redirect('summary3')
    return render(request, "CommanderDoc/formulaire4.html", {'mairies': mairies})





import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FormulaireDemandeActeNaissance, Transaction

@csrf_exempt
def valider_paiement(request):
    if request.method == "POST":
        data = json.loads(request.body)
        phone = data.get('phone')
        form_data = request.session.get('form_data')
        form_type = request.session.get('form_type')
        
        if not form_data or not form_type:
            return JsonResponse({'success': False, 'message': 'Aucune donnée de formulaire trouvée.'})

        # Log the form data for debugging
        print("Form Data:", form_data)

        # Enregistrer les données du formulaire en fonction du type de formulaire
        try:
            if form_type == 'formulaire2':
                formulaire = FormulaireDemandeActeNaissance(
                    user=request.user,
                    nom=form_data.get('nomPrenom'),
                    date_naissance=form_data.get('dateNaissance'),
                    lieu_de_naissance=form_data.get('lieuNaissance'),
                    numero_Acte=form_data.get('numExtrait'),
                    type_document=form_data.get('typenaissance'),
                    numero_cni=form_data.get('numCNI'),
                    email=form_data.get('email'),
                    tel=form_data.get('numTelephone'),
                    nombre=form_data.get('nbExemplaires'),
                    montant=form_data.get('total'),
                    livraison=form_data.get('modeLivraison'),
                    ville_de_livraison=form_data.get('ville'),
                    statut_commande='en_attente',
                    etat_commande='actif'
                )

            elif form_type == 'formulaire3':
                formulaire = FormulaireDemandeActeNaissance(
                    user=request.user,
                    non_prenom_epoux=form_data.get('nomPrenom'),
                    non_prenom_epouse=form_data.get('nomPrenom2'),
                    lieu_de_naissance=form_data.get('lieuNaissance'),
                    type_document=form_data.get('typenaissance'),
                    numero_Acte=form_data.get('numExtrait'),
                    numero_cni=form_data.get('numCNI'),
                    email=form_data.get('email'),
                    tel=form_data.get('numTelephone'),
                    nombre=form_data.get('nbExemplaires'),
                    montant=form_data.get('total'),
                    livraison=form_data.get('modeLivraison'),
                    ville_de_livraison=form_data.get('ville'),
                    statut_commande='en_attente',
                    etat_commande='actif'
                )

            elif form_type == 'formulaire4':
                formulaire = FormulaireDemandeActeNaissance(
                    user=request.user,
                    nom=form_data.get('nom'),
                    non_prenom_defunt=form_data.get('nomdefunt'),
                    date_naissance=form_data.get('dateNaissance'),
                    lieu_de_naissance=form_data.get('lieuNaissance'),
                    type_document=form_data.get('typenaissance'),
                    numero_Acte=form_data.get('numExtrait'),
                    numero_cni=form_data.get('numCNI'),
                    email=form_data.get('email'),
                    tel=form_data.get('numTelephone'),
                    nombre=form_data.get('nbExemplaires'),
                    montant=form_data.get('total'),
                    livraison=form_data.get('modeLivraison'),
                    ville_de_livraison=form_data.get('ville'),
                    statut_commande='en_attente',
                    etat_commande='actif'
                )
            else:
                return JsonResponse({'success': False, 'message': 'Type de formulaire inconnu.'})

            # Enregistrer le formulaire dans la base de données
            formulaire.save()
        except Exception as e:
            print("Error saving form:", str(e))
            return JsonResponse({'success': False, 'message': 'Erreur lors de l\'enregistrement du formulaire.'})

        # Enregistrer les informations de paiement
        try:
            transaction = Transaction(
                user=request.user,
                montant=form_data.get('total'),
                phone=phone,
                status='Réussie'
            )
            transaction.save()
        except Exception as e:
            print("Error saving transaction:", str(e))
            return JsonResponse({'success': False, 'message': 'Erreur lors de l\'enregistrement de la transaction.'})

        # Supprimer les données de la session
        del request.session['form_data']
        del request.session['form_type']

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'message': 'Méthode de requête non autorisée.'})




@login_required
def summary(request):
    form_data = request.session.get('form_data')
    form_type = request.session.get('form_type')

    if form_type != 'formulaire2' or not form_data:
        return HttpResponseBadRequest("Aucune donnée de formulaire trouvée ou type de formulaire incorrect.")

    return render(request, "CommanderDoc/summary.html", {'form_data': form_data})


@login_required
def summary2(request):
    form_data = request.session.get('form_data')
    form_type = request.session.get('form_type')

    if form_type != 'formulaire3' or not form_data:
        return HttpResponseBadRequest("Aucune donnée de formulaire trouvée ou type de formulaire incorrect.")

    return render(request, "CommanderDoc/summary2.html", {'form_data': form_data})


@login_required
def summary3(request):
    form_data = request.session.get('form_data')
    form_type = request.session.get('form_type')

    if form_type != 'formulaire4' or not form_data:
        return HttpResponseBadRequest("Aucune donnée de formulaire trouvée ou type de formulaire incorrect.")

    return render(request, "CommanderDoc/summary3.html", {'form_data': form_data})


@login_required
def supprimer_enregistrement(request):
    if request.method == 'POST':
        id_facture = request.POST.get('id_suprimer')
        facture = get_object_or_404(FormulaireDemandeActeNaissance, id=id_facture)
        # Modifier l'état de la commande en 'inactif'
        facture.etat_commande = 'inactif'
        facture.save()

    return redirect('tab')

@login_required
def dashe(request):
    user = request.user
    fact = FormulaireDemandeActeNaissance.objects.filter(user=user, etat_commande='actif')
    # Calculer le nombre d'utilisateurs inscrits
    nombre_visiteurs = CustomUser.objects.count()
    # Calculer le nombre de commandes
    nombre_commandes = FormulaireDemandeActeNaissance.objects.count()
    return render(request, "CommanderDoc/admindash.html",
                  {"user": user, "fact": fact, "nombre_visiteurs": nombre_visiteurs,
                   "nombre_commandes": nombre_commandes})

@login_required
def adminDash(request):
    user = request.user
    agent = None
    ville = None
    article = None
    nom_mairie = ""

    if hasattr(user, 'agent'):
        agent = user.agent
        ville = agent.mairie
        article = FormulaireDemandeActeNaissance.objects.filter(
            lieu_de_naissance=ville,
            statut_commande__in=['en_attente', 'valide']
        )
        nom_mairie = agent.mairie

    return render(request, 'CommanderDoc/dash_admin.html', {"article": article, "nom_mairie": nom_mairie})



def paiement(request, id_fact):
    fact = FormulaireDemandeActeNaissance.objects.get(id=id_fact)
    return render(request, "paiement.html", {"fact": fact})

@login_required
def detail_commande(request, user_id):
    commandes_utilisateur = FormulaireDemandeActeNaissance.objects.filter(user_id=user_id)
    return render(request, "CommanderDoc/detail_commande.html", {"commandes_utilisateur": commandes_utilisateur})


from django.shortcuts import redirect, get_object_or_404
from .models import FormulaireDemandeActeNaissance

def valider_commande(request, commande_id):
    commande = get_object_or_404(FormulaireDemandeActeNaissance, id=commande_id)
    commande.statut_commande = 'valide'
    commande.save()
    return redirect('dash_admin')  


def refuser_commande(request, commande_id):
    commande = get_object_or_404(FormulaireDemandeActeNaissance, id=commande_id)
    commande.statut_commande = 'refuse'
    commande.save()
    message_body = (
        f"Votre commande #{commande_id} a été refusée, "
        "motif: incohérence des informations. "
        "Vous serez remboursé dans de brefs délais."
    )
    
    Notification.objects.create(user=commande.user, message=message_body)
    
    return redirect('dash_admin')

def terminer_commande(request, commande_id):
    commande = get_object_or_404(FormulaireDemandeActeNaissance, id=commande_id)
    commande.statut_commande = 'termine'
    commande.save()
    
    if commande.livraison == 'presentiel':
        message_body = (
            f"Votre commande #{commande_id} est terminée. "
            "Vous pouvez venir récupérer votre commande. "
            "Merci d'avoir utilisé la_mairie_chez_vous."
        )
    elif commande.livraison == 'point de relais':
        message_body = (
            f"Votre commande #{commande_id} est terminée. "
            "Vous pouvez aller la récupérer dans votre point de relais choisi : "
            f"{commande.ville_de_livraison}. "
            "Merci d'avoir utilisé la_mairie_chez_vous."
        )
    elif commande.livraison == 'livraison':
        message_body = (
            f"Votre commande #{commande_id} est terminée. "
            "Un agent de livraison viendra vous livrer à cette adresse : "
            f"{commande.ville_de_livraison}. "
            "Merci d'avoir utilisé la_mairie_chez_vous."
        )
    
    Notification.objects.create(user=commande.user, message=message_body)
    
    return redirect('dash_admin')



from django.shortcuts import render
from .models import FormulaireDemandeActeNaissance


@login_required
def commande_valider(request):
    # Récupérer la mairie de l'utilisateur connecté
    mairie_utilisateur = request.user.agent.mairie
    # Récupérer toutes les commandes avec le statut_commande valide
    commandes_validees = FormulaireDemandeActeNaissance.objects.filter(lieu_de_naissance=mairie_utilisateur,
                                                                       statut_commande='valide', )
    return render(request, "CommanderDoc/commande_valider.html",
                  {'commandes_validees': commandes_validees, "nom_mairie": mairie_utilisateur})


@login_required
def commande_refuser(request):
    # Récupérer la mairie de l'utilisateur connecté
    mairie_utilisateur = request.user.agent.mairie
    # Récupérer toutes les commandes avec le statut_commande refusée
    commandes_refusees = FormulaireDemandeActeNaissance.objects.filter(lieu_de_naissance=mairie_utilisateur,
                                                                       statut_commande='refuse')
    return render(request, "CommanderDoc/commande_refuser.html",
                  {'commandes_refusees': commandes_refusees, "nom_mairie": mairie_utilisateur})


@login_required
def commande_terminer(request):
    # Récupérer la mairie de l'utilisateur connecté
    mairie_utilisateur = request.user.agent.mairie
    # Récupérer toutes les commandes avec le statut_commande terminée
    commandes_terminee = FormulaireDemandeActeNaissance.objects.filter(lieu_de_naissance=mairie_utilisateur,
                                                                       statut_commande='termine')
    return render(request, "CommanderDoc/commande_terminer.html",
                  {'commandes_terminee': commandes_terminee, "nom_mairie": mairie_utilisateur})


@login_required
def commande_attente(request):
    # Récupérer la mairie de l'utilisateur connecté
    mairie_utilisateur = request.user.agent.mairie
    # Récupérer toutes les commandes avec le statut_commande en attente
    commandes_attente = FormulaireDemandeActeNaissance.objects.filter(lieu_de_naissance=mairie_utilisateur,
                                                                      statut_commande='en_attente')
    return render(request, "CommanderDoc/commande_attente.html",
                  {'commandes_attente': commandes_attente, "nom_mairie": mairie_utilisateur})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import FormulaireDemandeActeNaissance

@login_required
def user(request):
    user = request.user
    agent = user.agent
    mairie_utilisateur = agent.mairie

    # Récupérer les commandes liées à la mairie de l'agent connecté
    commandes = FormulaireDemandeActeNaissance.objects.filter(lieu_de_naissance=mairie_utilisateur)

    # Obtenir le modèle d'utilisateur personnalisé
    CustomUser = get_user_model()

    # Récupérer les utilisateurs qui ont fait ces commandes
    utilisateurs_avec_commande = CustomUser.objects.filter(formulairedemandeactenaissance__in=commandes).distinct()

    return render(request, "CommanderDoc/user.html", { 
        "nom_mairie": mairie_utilisateur,
        "utilisateurs": utilisateurs_avec_commande
    })

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('page_accueil') 


from django.shortcuts import render
from .models import Notification

def notification(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'CommanderDoc/notification.html', {'notifications': notifications})


def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    if request.method == 'POST':
        notification.delete()
        messages.success(request, 'Notification supprimée avec succès.')
    return redirect('notification')



from django.http import JsonResponse
from .models import Notification


login_required
def get_unread_notification_count(request):
    unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
    return JsonResponse({'unread_count': unread_count})


@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notification')  # Rediriger vers la page des notifications

def paiement(request):
    if request.method == 'POST':
        montant = request.POST.get('montant')
        context = {
            'montant': montant,
        }
        return render(request, 'CommanderDoc/paiement.html', context)
    return redirect('formulaire')


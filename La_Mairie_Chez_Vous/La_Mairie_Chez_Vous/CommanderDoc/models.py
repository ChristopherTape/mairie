from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.conf import settings

class FormulaireDemandeActeNaissance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, null=True)
    non_prenom_epoux = models.CharField(max_length=200, null=True)
    non_prenom_epouse = models.CharField(max_length=200, null=True)
    non_prenom_defunt = models.CharField(max_length=200, null=True)
    date_naissance = models.DateField(null=True, blank=True)
    lieu_de_naissance = models.CharField(max_length=255 , null=True)
    type_document = models.CharField(max_length=100, default="valeur_par_defaut")
    numero_Acte = models.CharField(max_length=100)
    numero_cni = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    nombre = models.IntegerField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    livraison = models.CharField(max_length=100)
    ville_de_livraison = models.CharField(max_length=100, null=True, blank=True)
    date_commande = models.DateTimeField(auto_now_add=True)

    STATUT_CHOICES = (
        ('en_attente', 'En attente'),
        ('valide', 'Validée'),
        ('refuse', 'Refusée'),
        ('termine', 'Terminée'),
    )
    statut_commande = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')

    ETAT_CHOICES = (
        ('actif', 'actif'),
        ('inactif', 'inactif'),
    )
    etat_commande = models.CharField(max_length=20, choices=ETAT_CHOICES, default='actif')

    def __str__(self):
        return f"{self.nom}"

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.user.username} - {self.montant} - {self.status}"



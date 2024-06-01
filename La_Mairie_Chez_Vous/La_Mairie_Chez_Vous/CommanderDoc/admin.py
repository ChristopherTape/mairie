from django.contrib import admin
from .models import FormulaireDemandeActeNaissance, Transaction, Notification


@admin.register(FormulaireDemandeActeNaissance)
class FormAdmin(admin.ModelAdmin):
    list_display = ['user_id','nom','lieu_de_naissance',"statut_commande","montant","tel"]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'montant', 'phone', 'status']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'message', 'created_at', 'is_read']
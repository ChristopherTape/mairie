from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Commander, name="CommanderDoc-commander"),
    path('Commander/', Commander, name="CommanderDoc-commander"),
    path('formulaire2', formulaire2, name='formulaire2'),
    path('formulaire3', formulaire3, name='formulaire3'),
    path('formulaire4', formulaire4, name='formulaire4'),
    path('summary', summary, name='summary'),
    path('summary2', summary2, name='summary2'),
    path('summary3', summary3, name='summary3'),
    path('Authentification/Authentification/Commander', Commander, name="CommanderDoc-commander"),
    path("tab/", dashe, name="tab"),
    path('admin_dashbord/', adminDash, name='dash_admin'),
    path('notification/', notification, name='notification'),
    path('notification/delete/<int:notification_id>/', delete_notification, name='delete_notification'),
    path('notification/read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
    path('notification/unread_count/', get_unread_notification_count, name='get_unread_notification_count'),
    path('supprimer-enregistrement/', supprimer_enregistrement, name='supprimer_enregistrement'),
    path('detail_commande/<int:user_id>/', detail_commande, name="detail_commande"),
    path('valider_commande/<int:commande_id>/', valider_commande, name='valider_commande'),
    path('refuser_commande/<int:commande_id>/', refuser_commande, name='refuser_commande'),
    path('terminer_commande/<int:commande_id>/', terminer_commande, name='terminer_commande'),
    path('commande_valider', commande_valider, name="commande_valider"),
    path('commande_refuser/', commande_refuser, name="commande_refuser"),
    path('commande_terminer/', commande_terminer, name="commande_terminer"),
    path('commande_attente/', commande_attente, name="commande_attente"),
    path('user/', user, name='user'),
    path('adminLMVC/', admin.site.urls, name='admin:index'),
    path('logout/', logout_view, name='logout'),
    path('payement/', paiement, name='page_de_payement'),
    path('valider_paiement/', valider_paiement, name='valider_paiement'),


]

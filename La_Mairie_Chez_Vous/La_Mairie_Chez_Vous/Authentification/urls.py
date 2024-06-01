
from django.urls import path, include
from django.urls import path
from .views import *

urlpatterns = [
    path('', connexion, name="Authentification-Connexion"),
    path('inscription/', inscription, name="Authentification-inscription"),
    path('Commander/', include("CommanderDoc.urls"), name="CommanderDoc-commander"),
    path('connexion/', connexion, name='connexion'),
    path('Authentification/Authentification/Commander', connexion),
    path('Authentification/inscription', inscription),
    # path('Connexion2/', Connexion2, name="Connexion2")
    path("new_passe/",password_reset_request,name='new_passe'),
    path("changer/", change_password, name='changer_mdp'),
    path("page/",notif,name="notif")

]
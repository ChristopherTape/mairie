
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [

    path('', index, name="page_accueil"),
    path('Authentification/', include("Authentification.urls")),
    path('Authentification/Connexion', include("Authentification.urls")),
    path('Authentification/Authentification/Commander', include("CommanderDoc.urls")),
    path('formulaire1/', include("CommanderDoc.urls")),
    path('user/', include("dashboard.urls")),
    path('Authentification/inscription/Commander/', include("CommanderDoc.urls")),
    path('Commander/', include("CommanderDoc.urls")),
    path('SuivreCom/', include("SuivreCom.urls")),
    path('dash/', include("dashboard.urls")),
    path('admin/', admin.site.urls, name="admin"),


    

]


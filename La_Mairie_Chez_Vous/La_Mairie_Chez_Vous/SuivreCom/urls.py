from django.urls import path
from .views import SuivreCom

urlpatterns = [
    path('', SuivreCom, name="SuivreCom-Suivrecommande")

]
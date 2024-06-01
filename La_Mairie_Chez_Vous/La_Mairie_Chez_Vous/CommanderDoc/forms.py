# forms.py

from django import forms
from .models import FormulaireDemandeActeNaissance

class FormulaireDemandeActeNaissanceForm(forms.ModelForm):
    class Meta:
        model = FormulaireDemandeActeNaissance
        fields = '__all__'




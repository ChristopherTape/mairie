from django import forms


class InscriptionForm(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    mot_de_passe = forms.CharField(widget=forms.PasswordInput)
    confirmation_mot_de_passe = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        mot_de_passe = cleaned_data.get("mot_de_passe")
        confirmation_mot_de_passe = cleaned_data.get("confirmation_mot_de_passe")

        # Vérifie si les mots de passe correspondent
        if mot_de_passe != confirmation_mot_de_passe:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")


class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "Votre email",
            }
        )

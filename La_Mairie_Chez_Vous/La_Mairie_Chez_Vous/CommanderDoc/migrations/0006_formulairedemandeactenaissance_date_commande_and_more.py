# Generated by Django 5.0.4 on 2024-05-15 21:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommanderDoc', '0005_alter_formulairedemandeactenaissance_lieu_de_naissance'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulairedemandeactenaissance',
            name='date_commande',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulairedemandeactenaissance',
            name='statut_commande',
            field=models.CharField(choices=[('en_attente', 'En attente'), ('valide', 'Validée'), ('refuse', 'Refusée'), ('termine', 'Terminée')], default='en_attente', max_length=20),
        ),
    ]
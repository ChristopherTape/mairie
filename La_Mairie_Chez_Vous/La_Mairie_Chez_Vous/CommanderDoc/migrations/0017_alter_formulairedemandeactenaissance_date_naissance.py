# Generated by Django 5.0.1 on 2024-05-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "CommanderDoc",
            "0016_formulairedemandeactenaissance_non_prenom_defunt_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulairedemandeactenaissance",
            name="date_naissance",
            field=models.DateField(blank=True, null=True),
        ),
    ]

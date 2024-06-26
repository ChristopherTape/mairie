# Generated by Django 5.0.3 on 2024-05-12 10:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Authentification", "0001_initial"),
        ("CommanderDoc", "0003_formulairedemandeactenaissance_mairie"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="formulairedemandeactenaissance",
            name="mairie",
        ),
        migrations.AlterField(
            model_name="formulairedemandeactenaissance",
            name="lieu_de_naissance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="Authentification.agent",
            ),
        ),
        migrations.AlterField(
            model_name="formulairedemandeactenaissance",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

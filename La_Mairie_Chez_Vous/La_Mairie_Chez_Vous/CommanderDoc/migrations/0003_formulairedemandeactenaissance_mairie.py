# Generated by Django 5.0.4 on 2024-05-11 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Authentification", "0001_initial"),
        ("CommanderDoc", "0002_alter_formulairedemandeactenaissance_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="formulairedemandeactenaissance",
            name="mairie",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="Authentification.agent",
            ),
        ),
    ]

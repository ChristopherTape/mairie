# Generated by Django 5.0.4 on 2024-05-10 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommanderDoc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulairedemandeactenaissance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
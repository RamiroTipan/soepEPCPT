# Generated by Django 3.2.6 on 2022-01-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0054_auto_20220120_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitados',
            name='estado_invitado',
            field=models.CharField(choices=[('02', 'Invitado'), ('01', 'Adjudicado')], default='02', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('03', 'Fallido'), ('02', 'Adjudicado'), ('01', 'En Trámite')], default='01', max_length=2),
        ),
    ]

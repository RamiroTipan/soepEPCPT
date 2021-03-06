# Generated by Django 3.2.6 on 2021-12-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0039_alter_invitaciones_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitados',
            name='estado_invitado',
            field=models.CharField(choices=[('01', 'Adjudicado'), ('02', 'Invitado')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('02', 'Adjudicado'), ('03', 'Fallido'), ('01', 'En Proceso')], default='01', max_length=2),
        ),
    ]

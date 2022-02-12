# Generated by Django 3.2.6 on 2022-01-06 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0050_auto_20220106_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjudica',
            name='ganador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.invitados', verbose_name='Ganador'),
        ),
        migrations.AlterField(
            model_name='adjudica',
            name='invitacion_ad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.invitaciones', verbose_name='Invitación'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('02', 'Adjudicado'), ('01', 'En Proceso'), ('03', 'Fallido')], default='01', max_length=2),
        ),
    ]

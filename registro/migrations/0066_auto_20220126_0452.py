# Generated by Django 3.2.6 on 2022-01-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0065_auto_20220125_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='estado_p',
            field=models.CharField(choices=[('01', 'Análisis'), ('02', 'Ejecución'), ('03', 'Finalizado')], default='01', help_text='Escoja un estado', max_length=2),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='observaciones',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='invitados',
            name='estado_invitado',
            field=models.CharField(choices=[('02', 'Invitado'), ('01', 'Adjudicado')], default='02', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('01', 'En Trámite'), ('03', 'Fallido'), ('02', 'Adjudicado')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='tipo_contratacion',
            field=models.CharField(choices=[('02', 'Fiscalizaciòn'), ('01', 'Construcción')], default='01', max_length=2),
        ),
    ]
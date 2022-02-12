# Generated by Django 3.2.6 on 2021-12-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0044_auto_20211224_1548'),
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
            field=models.CharField(choices=[('01', 'En Proceso'), ('03', 'Fallido'), ('02', 'Adjudicado')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='tipo_contratacion',
            field=models.CharField(choices=[('01', 'Construcción'), ('02', 'Fiscalizaciòn')], default='01', max_length=2),
        ),
    ]

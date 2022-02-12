# Generated by Django 3.2.6 on 2022-01-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0052_auto_20220106_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjudica',
            name='ganador',
            field=models.CharField(max_length=10, null=True, verbose_name='Ganador'),
        ),
        migrations.AlterField(
            model_name='invitados',
            name='estado_invitado',
            field=models.CharField(choices=[('01', 'Adjudicado'), ('02', 'Invitado')], default='02', max_length=2),
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
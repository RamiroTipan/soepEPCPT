# Generated by Django 3.2.6 on 2021-12-06 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0032_auto_20211206_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='Fecha_publica',
            field=models.DateField(verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('01', 'En Proceso'), ('03', 'Fallido'), ('02', 'Adjudicado')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='tipo_contratacion',
            field=models.CharField(choices=[('02', 'Fiscalizaciòn'), ('01', 'Construcción')], default='01', max_length=2),
        ),
    ]

# Generated by Django 3.2.6 on 2021-12-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0031_auto_20211204_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proceso',
            name='resolucion',
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('03', 'Fallido'), ('01', 'En Proceso'), ('02', 'Adjudicado')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='tipo_contratacion',
            field=models.CharField(choices=[('01', 'Construcción'), ('02', 'Fiscalizaciòn')], default='01', max_length=2),
        ),
    ]

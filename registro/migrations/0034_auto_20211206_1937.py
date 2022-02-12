# Generated by Django 3.2.6 on 2021-12-07 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0033_auto_20211206_1423'),
    ]

    operations = [
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

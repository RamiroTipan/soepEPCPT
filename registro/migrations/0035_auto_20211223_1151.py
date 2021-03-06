# Generated by Django 3.2.6 on 2021-12-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0034_auto_20211206_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitaciones',
            options={'ordering': ['id'], 'verbose_name': 'Invitacion', 'verbose_name_plural': 'Invitaciones'},
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('01', 'En Proceso'), ('03', 'Fallido'), ('02', 'Adjudicado')], default='01', max_length=2),
        ),
    ]

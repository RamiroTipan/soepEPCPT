# Generated by Django 3.2.6 on 2021-12-05 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0030_auto_20211204_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canton',
            name='rel_prov_canton',
            field=models.ForeignKey(blank=True, db_column='id_user', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.provincia'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('03', 'Fallido'), ('02', 'Adjudicado'), ('01', 'En Proceso')], default='01', max_length=2),
        ),
    ]
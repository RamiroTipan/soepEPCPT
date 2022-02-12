# Generated by Django 3.2.6 on 2022-01-25 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0064_auto_20220125_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitaciones',
            name='relacion_procesoi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='registro.proceso', verbose_name='Proceso'),
        ),
        migrations.AlterField(
            model_name='invitaciones',
            name='relacion_usuarioi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='invita', to=settings.AUTH_USER_MODEL, verbose_name='Encargado'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('03', 'Fallido'), ('02', 'Adjudicado'), ('01', 'En Trámite')], default='01', max_length=2),
        ),
    ]
# Generated by Django 3.2.6 on 2022-01-25 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0063_auto_20220125_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitaciones',
            name='relacion_procesoi',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='registro.proceso', verbose_name='Proceso'),
        ),
        migrations.AlterField(
            model_name='invitaciones',
            name='relacion_usuarioi',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, related_name='invita', to='registro.usuario', verbose_name='Encargado'),
        ),
        migrations.AlterField(
            model_name='invitados',
            name='estado_invitado',
            field=models.CharField(choices=[('01', 'Adjudicado'), ('02', 'Invitado')], default='02', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('03', 'Fallido'), ('01', 'En Trámite'), ('02', 'Adjudicado')], default='01', max_length=2),
        ),
    ]

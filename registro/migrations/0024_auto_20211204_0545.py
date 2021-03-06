# Generated by Django 3.2.6 on 2021-12-04 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0023_auto_20211201_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyectos',
            old_name='monto',
            new_name='monto_ref',
        ),
        migrations.RemoveField(
            model_name='proceso',
            name='Fecha_apertura',
        ),
        migrations.RemoveField(
            model_name='proceso',
            name='Fecha_lim_audpr',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='monto_experiencia',
        ),
        migrations.AddField(
            model_name='proceso',
            name='monto_experiencia',
            field=models.DecimalField(decimal_places=2, default=154, max_digits=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitaciones',
            name='relacion_usuarioi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='invita', to=settings.AUTH_USER_MODEL, verbose_name='Encargado'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('02', 'Adjudicado'), ('03', 'Fallido'), ('01', 'En Proceso')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='tipo_contratacion',
            field=models.CharField(choices=[('02', 'Fiscalizaciòn'), ('01', 'Construcción')], default='01', max_length=2),
        ),
    ]

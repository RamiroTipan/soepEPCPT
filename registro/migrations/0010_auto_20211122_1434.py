# Generated by Django 3.2.6 on 2021-11-22 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0009_auto_20211121_1223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitaciones',
            options={'ordering': ['relacion_procesoi'], 'verbose_name': 'Invitacion', 'verbose_name_plural': 'Invitaciones'},
        ),
        migrations.RemoveField(
            model_name='invitaciones',
            name='relacion_proyectoi',
        ),
        migrations.AddField(
            model_name='invitaciones',
            name='relacion_procesoi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='registro.proceso', verbose_name='Proceso'),
        ),
        migrations.AlterField(
            model_name='natural',
            name='genero',
            field=models.CharField(choices=[('02', 'Femenico'), ('01', 'Masculino')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('02', 'Adjudicado'), ('03', 'Fallido'), ('01', 'En Proceso')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='tipo_contratacion',
            field=models.CharField(choices=[('01', 'Construcción'), ('02', 'Fiscalizaciòn')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='relacion_canton',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='registro.canton', verbose_name='Cantón'),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='relacion_provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='registro.provincia', verbose_name='Provincia'),
        ),
    ]

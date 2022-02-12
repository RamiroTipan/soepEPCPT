# Generated by Django 3.2.6 on 2021-09-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_invitaciones'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitaciones',
            options={'ordering': ['relacion_proyectoi'], 'verbose_name': 'Invitacion', 'verbose_name_plural': 'Invitaciones'},
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='fecha_creacion',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_persona',
            field=models.CharField(choices=[('02', 'Jurídica'), ('01', 'Natural')], default='01', max_length=2),
        ),
    ]

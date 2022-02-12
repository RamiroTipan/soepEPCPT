# Generated by Django 3.2.6 on 2021-09-17 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20210917_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='relacion_proyectos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='registro.proyectos', verbose_name='Proyecto'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='tipo_contratacion',
            field=models.CharField(choices=[('01', 'Construcción'), ('02', 'Fiscalizaciòn')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_persona',
            field=models.CharField(choices=[('01', 'Natural'), ('02', 'Jurídica')], default='01', max_length=2),
        ),
    ]
# Generated by Django 3.2.6 on 2021-12-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0025_auto_20211204_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='Fecha_adjudica',
            field=models.DateTimeField(verbose_name='Fecha estimada de adjudicación'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='Fecha_propuesta',
            field=models.DateTimeField(verbose_name='Fecha de entrega de propuestas'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='Fecha_publica',
            field=models.DateTimeField(verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.CharField(choices=[('03', 'Fallido'), ('01', 'En Proceso'), ('02', 'Adjudicado')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='plazo_entrega',
            field=models.IntegerField(verbose_name='Plazo de entrega (meses)'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-01 00:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_remove_documental_fecha_remove_pelicula_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documental',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pelicula',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serie',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documental',
            name='duracion',
            field=models.IntegerField(verbose_name='Duración (minutos)'),
        ),
        migrations.AlterField(
            model_name='documental',
            name='tipo',
            field=models.CharField(max_length=40, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.IntegerField(verbose_name='Duración (minutos)'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='tipo',
            field=models.CharField(max_length=20, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='tipo',
            field=models.CharField(max_length=40, verbose_name='Género'),
        ),
    ]

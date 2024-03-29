# Generated by Django 4.0.5 on 2022-07-25 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoJuegoApp', '0003_imgperfil_delete_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('descripcion', models.CharField(max_length=110, verbose_name='Descripcion')),
                ('imagen', models.URLField(blank=255, max_length=255)),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoJuegoApp.jugador')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoJuegoApp.juego')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]

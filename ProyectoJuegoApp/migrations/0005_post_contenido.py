# Generated by Django 4.0.5 on 2022-07-25 19:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoJuegoApp', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(default='Some string', verbose_name='Contenido'),
        ),
    ]
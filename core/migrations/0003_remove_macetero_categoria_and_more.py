# Generated by Django 4.0.1 on 2022-06-08 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='macetero',
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='tierradehoja',
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='flores',
        ),
        migrations.DeleteModel(
            name='macetero',
        ),
        migrations.DeleteModel(
            name='tierradehoja',
        ),
    ]

# Generated by Django 4.0.1 on 2022-06-08 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('sku', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='SKU')),
                ('nombreProducto', models.CharField(max_length=20, verbose_name='Nombre del producto')),
                ('precio', models.CharField(max_length=20, verbose_name='Precio')),
                ('Stock', models.CharField(blank=True, max_length=20, null=True, verbose_name='Stock disponible')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]

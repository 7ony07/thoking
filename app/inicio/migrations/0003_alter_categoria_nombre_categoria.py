# Generated by Django 4.2.7 on 2023-11-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_categoria_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre_categoria',
            field=models.CharField(max_length=60, verbose_name='Nombre Categoria'),
        ),
    ]

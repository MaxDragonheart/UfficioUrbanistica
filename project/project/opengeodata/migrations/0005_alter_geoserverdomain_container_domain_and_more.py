# Generated by Django 4.1.4 on 2022-12-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opengeodata', '0004_geoserverdomain_container_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoserverdomain',
            name='container_domain',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='geoserverdomain',
            name='domain',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]

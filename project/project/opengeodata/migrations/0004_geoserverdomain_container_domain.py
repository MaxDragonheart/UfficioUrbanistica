# Generated by Django 4.1.4 on 2022-12-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opengeodata', '0003_alter_geoserverdomain_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoserverdomain',
            name='container_domain',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
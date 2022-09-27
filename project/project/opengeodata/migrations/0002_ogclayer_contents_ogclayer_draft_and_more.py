# Generated by Django 4.1.1 on 2022-09-27 08:31

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('opengeodata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ogclayer',
            name='contents',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ogclayer',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ogclayer',
            name='highlighted',
            field=models.BooleanField(default=False),
        ),
    ]
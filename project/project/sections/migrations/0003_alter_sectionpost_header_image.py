# Generated by Django 4.1.1 on 2022-09-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpost',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/%Y/%m/%d'),
        ),
    ]
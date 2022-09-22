# Generated by Django 4.1.1 on 2022-09-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_fileupload_highlighted'),
        ('sections', '0003_alter_sectionpost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionpost',
            name='attachment',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_attachment', to='media.fileupload'),
        ),
    ]

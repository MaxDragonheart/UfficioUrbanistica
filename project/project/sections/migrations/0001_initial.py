# Generated by Django 4.1.1 on 2022-09-22 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug_category', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Sezione',
                'verbose_name_plural': 'Sezioni',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='SectionPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=70, unique=True)),
                ('slug_post', models.SlugField(max_length=70, unique=True)),
                ('header_image', models.ImageField(default='header_default.jpg', upload_to='uploads/images/%Y/%m/%d')),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('contents', tinymce.models.HTMLField(blank=True, null=True)),
                ('draft', models.BooleanField(default=False)),
                ('highlighted', models.BooleanField(default=False)),
                ('attachment', models.ManyToManyField(blank=True, related_name='related_attachment', to='media.fileupload')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='related_category', to='sections.section')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='related_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pubblicazione',
                'verbose_name_plural': 'Pubblicazioni',
                'ordering': ['-publishing_date'],
            },
        ),
    ]

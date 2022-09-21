from django.db import models
from django.utils import timezone

import os
from tinymce import models as tinymce_models


class TimeManager(models.Model):
    """
    Definizione dello standard tempo
    """
    publishing_date = models.DateTimeField(default=timezone.now)
    updating_date = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    @property
    def is_future(self):
        """
        Funzione che verifica se un post è da pubblicare nel futuro o subito
        """
        if self.publishing_date > timezone.now():
            return True
        return False

    class Meta:
        abstract = True


class CategoryBase(TimeManager):
    """
    definizione delle caratteristiche di una categoria
    """
    category_name = models.CharField(max_length=50, unique=True)
    slug_category = models.SlugField(unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        abstract = True


class BaseModelPost(TimeManager):
    """
    Modello base per i post.
    """
    title = models.CharField(max_length=70, unique=True)
    slug_post = models.SlugField(max_length=70, unique=True)
    header_image = models.ImageField(upload_to='uploads/images/%Y/%m/%d', default='header_default.jpg')
    description = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class ModelPost(BaseModelPost):
    """
    Con questa classe definisco le caratteristiche
    comuni dei post
    """
    contents = tinymce_models.HTMLField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)

    class Meta:
        abstract = True

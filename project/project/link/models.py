from django.db import models

from abstracts.models import TimeManager


class Link(TimeManager):

    COLUMNS = [
        ('Colonna 1', 1),
        ('Colonna 2', 2),
        ('Colonna 3', 3),
    ]

    title = models.CharField(max_length=70, unique=True)
    description = models.TextField(max_length=150, blank=False, null=False)
    url = models.URLField(unique=True)
    column = models.CharField(max_length=10, choices=COLUMNS, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Link Utile"
        verbose_name_plural = "Link Utili"
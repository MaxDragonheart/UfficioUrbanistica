from django.db import models
from django.urls import reverse

from abstracts.models import CategoryBase, ModelPost


class Section(CategoryBase):
    """
    Questa classe definisce le caratteristiche di
    una categoria
    """

    def get_absolute_url(self):
        return reverse("single_category", kwargs={"slug_category": self.slug_category})

    class Meta:
        ordering = ['category_name']
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"


class SectionPost(ModelPost):
    """
    Questa classe definisce le caratteristiche di
    un post del blog
    """
    category = models.ForeignKey(Section, on_delete=models.PROTECT, related_name="related_category")

    def get_absolute_url(self):
        return reverse("single_article", kwargs={
                                                "slug_post": self.slug_post,
                                                "slug_category": self.category.slug_category,
                                                })

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "Pubblicazione"
        verbose_name_plural = "Pubblicazioni"

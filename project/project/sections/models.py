from django.db import models
from django.urls import reverse

from abstracts.models import CategoryBase, ModelPost


class BlogCategory(CategoryBase):
    """
    Questa classe definisce le caratteristiche di
    una categoria
    """

    def get_absolute_url(self):
        return reverse("single_blogcategory", kwargs={"slug_category": self.slug_category})

    class Meta:
        ordering = ['category_name']
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"


class BlogPost(ModelPost):
    """
    Questa classe definisce le caratteristiche di
    un post del blog
    """
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, related_name="related_blogcategory")

    def get_absolute_url(self):
        return reverse("single_blogpost", kwargs={
                                                "slug_post": self.slug_post,
                                                "slug_category": self.category.slug_category,
                                                })

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "Pubblicazione"
        verbose_name_plural = "Pubblicazioni"

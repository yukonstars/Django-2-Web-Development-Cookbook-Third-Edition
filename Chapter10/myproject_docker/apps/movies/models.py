from datetime import datetime

from django.core.validators import (MaxValueValidator,
                                    MinValueValidator)
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey, TreeManyToManyField

from utils.models import CreationModificationDateMixin

RATING_CHOICES = (
    (1, "★☆☆☆☆☆☆☆☆☆"),
    (2, "★★☆☆☆☆☆☆☆☆"),
    (3, "★★★☆☆☆☆☆☆☆"),
    (4, "★★★★☆☆☆☆☆☆"),
    (5, "★★★★★☆☆☆☆☆"),
    (6, "★★★★★★☆☆☆☆"),
    (7, "★★★★★★★☆☆☆"),
    (8, "★★★★★★★★☆☆"),
    (9, "★★★★★★★★★☆"),
    (10, "★★★★★★★★★★"),
)


class Category(MPTTModel, CreationModificationDateMixin):
    class Meta:
        ordering = ["tree_id", "lft"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    class MPTTMeta:
        order_insertion_by = ["title"]

    parent = TreeForeignKey("self",
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True,
                            related_name="children")
    title = models.CharField(_("Title"),
                             max_length=200)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(_("Title"),
                             max_length=100)

    def __str__(self):
        return self.title


class Director(models.Model):
    first_name = models.CharField(_("First name"),
                                  max_length=40)
    last_name = models.CharField(_("Last name"),
                                 max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(_("First name"),
                                  max_length=40)
    last_name = models.CharField(_("Last name"),
                                 max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    class Meta:
        ordering = ["title"]
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    title = models.CharField(
        _("Title"),
        max_length=255)
    genres = models.ManyToManyField(
        Genre,
        blank=True)
    directors = models.ManyToManyField(
        Director,
        blank=True)
    actors = models.ManyToManyField(
        Actor,
        blank=True)
    release_year = models.PositiveSmallIntegerField(
        _("Release year"),
        validators=[MinValueValidator(1888),
                    MaxValueValidator(datetime.now().year)],
        default=datetime.now().year)
    rating = models.DecimalField(
        _("Rating"),
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0),
                    MaxValueValidator(10)])
    rank = models.PositiveIntegerField(
        unique=True,
        blank=False,
        null=False,
        default=0)
    featured = models.BooleanField(default=False)
    commercial = models.BooleanField(default=False)
    independent = models.BooleanField(default=False)
    categories = TreeManyToManyField(Category,
                                     verbose_name=_("Categories"),
                                     blank=True)

    @property
    def rating_percentage(self):
        """Convert 0-10 rating into a 0-100 percentage"""
        return int(self.rating * 10)

    def __str__(self):
        return self.title

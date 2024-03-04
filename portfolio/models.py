from django.db import models as m
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.text import slugify


class Projet(m.Model):
    name = m.CharField(max_length=50, unique=True)
    ordre = m.PositiveIntegerField()
    slug = m.SlugField(max_length=50, unique=True)
    description = m.TextField()
    image = m.ImageField(upload_to="Projets")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Projet, self).save(*args, **kwargs)

    @property
    def short_description(self):
        return truncatechars(self.description, 50)

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        return reverse('projet', kwargs={'slug': self.slug})


class PageProject(m.Model):
    projet = m.ForeignKey(Projet, on_delete=m.CASCADE, related_name='Pages')
    ordre = m.PositiveIntegerField()
    description = m.TextField()
    image = m.ImageField(upload_to="PagesProject", blank=True, null=True)

    def __str__(self) -> str:
        return f"Page {self.ordre} du projet {self.projet.name}"

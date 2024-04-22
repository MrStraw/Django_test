from pathlib import Path

from django.db import models as m
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.text import slugify


def get_upload_path(instance, filename):
    if isinstance(instance, Projet):
        return Path('Projets', instance.slug, f'Couverture__{filename}')
    elif isinstance(instance, PageProject):
        return Path('Projets', instance.projet.slug, f'Page-{instance.ordre}__{filename}')


class Projet(m.Model):
    name = m.CharField(max_length=50, unique=True)
    ordre = m.PositiveIntegerField()
    slug = m.SlugField(max_length=50, unique=True)
    description = m.TextField()
    image = m.ImageField(upload_to=get_upload_path)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.ordre is None:
            self.ordre = len(Projet.objects.all()) + 1
        super().save()

    @property
    def is_visible(self) -> bool:
        return bool(self.ordre)

    @property
    def short_description(self):
        return truncatechars(self.description, 50)

    def get_absolute_url(self):
        return reverse('projet', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return str(self.name)


class PageProject(m.Model):
    projet = m.ForeignKey(Projet, on_delete=m.CASCADE, related_name='Pages')
    ordre = m.PositiveIntegerField()
    titre = m.CharField(max_length=50)
    sous_titre = m.CharField(max_length=50)
    description = m.TextField()
    image = m.ImageField(upload_to=get_upload_path, blank=True, null=True)

    def __str__(self) -> str:
        return f"Page {self.ordre} du projet {self.projet.name}"

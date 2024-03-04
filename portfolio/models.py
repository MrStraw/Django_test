from django.db import models as m
from django.urls import reverse


class Projet(m.Model):
    name = m.CharField(max_length=50, unique=True)
    ordre = m.IntegerField()
    slug = m.SlugField(max_length=50, unique=True)
    description = m.TextField()
    image = m.ImageField(upload_to="Projets")

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        return reverse('projet', kwargs={'slug': self.slug})


class PageProject(m.Model):
    projet = m.ForeignKey(Projet, on_delete=m.CASCADE, related_name='Pages')
    ordre = m.IntegerField()
    description = m.TextField()
    image = m.ImageField(upload_to="PagesProject", blank=True, null=True)

    def __str__(self) -> str:
        return f"Page {self.ordre} du projet {self.projet.name}"

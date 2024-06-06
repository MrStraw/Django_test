from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from portfolio.models import Projet


def home(request):
    projets = Projet.objects.filter(ordre__gt=0).order_by('ordre')
    return render(request, 'home.html', context={'projets': projets})


def projets_index(request):
    response = redirect('/#projets')
    return response


def projets_details(request, slug):
    projet = get_object_or_404(Projet, slug=slug)
    if not projet.is_visible:
        raise Http404("Projet non publique.")
    context = {
        'projet': projet,
        'pages': projet.Pages.filter(ordre__gt=0).order_by('ordre')
    }
    return render(request, 'projet.html', context=context)

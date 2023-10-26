from django.shortcuts import render
from django.shortcuts import render
from .models import FORET


def home_page(request, nom_foret):
    try:
        foret = FORET.objects.get(nom_foret=nom_foret)
    except FORET.DoesNotExist:
        foret = None

    context = {
        'foret': foret
    }

    return render(request, 'home_page.html', context)
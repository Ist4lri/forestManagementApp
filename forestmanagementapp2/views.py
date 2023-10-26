
from .models import FORET

from .forms.forms import ForetForm
from django.shortcuts import render
from .forms.forms import ForetForm


def enter_forest(request):
    if request.method == 'POST':
        form = ForetForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegardez les données ici
            # Vous pouvez rediriger l'utilisateur vers une autre page après la soumission

    else:
        form = ForetForm()

    return render(request, 'enter_forest.html', {'form': form})


def home_page(request, nom_foret):
    try:
        foret = FORET.objects.get(nom_foret=nom_foret)
    except FORET.DoesNotExist:
        foret = None

    context = {
        'foret': foret
    }

    return render(request, 'home_page.html', context)
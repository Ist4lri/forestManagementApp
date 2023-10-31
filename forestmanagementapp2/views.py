
import os
import random
from django.shortcuts import render, redirect
from .forms import PostFormIncident, PostFormOrganism, ForestForm
from .models import Foret
import re
from django.db.models import Q


from django.shortcuts import render, redirect
from .models import Foret
from .forms import ForestForm

def enter_forest(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    forets = Foret.objects.all()
    foret = None

    if request.method == 'POST':
        form = ForestForm(request.POST)
        if form.is_valid():
            foretclean = form.cleaned_data['nom_foret']
            # Recherche de la forêt avec le nom_foret correspondant
            try:
                foret = Foret.objects.get(nom_foret=foretclean)
                return redirect('home_page', nom_foret=foret)
            except Foret.DoesNotExist:
                foret = None  # Si la forêt n'est pas trouvée, foret est None

    else:
        form = ForestForm()

    return render(request, 'enter_forest.html', {'foret': form, 'forets': forets, 'image_path': image_path, 'foret_result': foret})

def home_page(request, nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    foret = Foret.objects.get(nom_foret=nom_foret)
    description = foret.get_description()
    return render(request, 'home_page.html', {'nom_foret':nom_foret, 'image_path':image_path,'description':description})


def randomImage():
    return [fichier for fichier in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/forest_pic')) if fichier.lower().endswith(('.jpeg'))]


def v_form_submitted(request, image_path="/forest_pic/for1.jpeg"):
    return render(request, 'formSubmitted.html', {'image_path': image_path})


def v_post_new_incident(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == "POST":
        form = PostFormIncident(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.statut_incident = "En cours"
            post.save(using='forestDB')
            return redirect('formSubmitted', image_path)
    else:
        form = PostFormIncident()
    return render(request, 'incidentForm.html', {
        'image_path': image_path,
        'title_page': "Formulaire d'incident",
        'title_form': "Décrivez l'incident",
        'description_form': "Veuillez décrire l'incident que vous avez vus, et indiquer le lieu en question.",
        'form': form,
    })


def v_register_new_species(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == "POST":
        form = PostFormOrganism(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save(using='forestDB')
            return redirect('formSubmitted', image_path)
    else:
        form = PostFormOrganism()
    return render(request, 'incidentForm.html', {
        'image_path': image_path,
        'title_page': "Formulaire de nouvelle espèce",
        'title_form': "Détailler une nouvelle espèce dans une forêt.",
        'description_form': "Veuillez remplir les champs demandé tel que demandé dans le protocole.",
        'form': form,
    })




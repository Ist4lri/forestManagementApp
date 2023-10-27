
import os
import random
from django.shortcuts import render, redirect
from .forms import PostFormIncident, PostFormOrganism, ForestForm
from .models import FORET
from django.http import Http404
from fuzzywuzzy import fuzz



def enter_forest(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    forets = FORET.objects.values_list('nom_foret', flat=True)
    if request.method == 'POST':
        form = ForestForm(request.POST)
        if form.is_valid():
            form.save()
            nom_foret = form.cleaned_data['nom_foret'].strip()
            return redirect('home_page', nom_foret=nom_foret)
    else:
        form = ForestForm()
    return render(request, 'enter_forest.html', {'form': form, 'forets': forets, 'image_path':image_path})

def find_closest_forest(nom_foret):
    closest_match = None
    highest_similarity = 0

    for foret in FORET.objects.all():
        similarity = fuzz.ratio(nom_foret, foret.nom_foret)
        if similarity > highest_similarity:
            highest_similarity = similarity
            closest_match = foret

    return closest_match
def home_page(request, nom_foret):
    closest_foret = find_closest_forest(nom_foret)

    if closest_foret:
        context = {
            'nom_foret': closest_foret.nom_foret
        }
        return render(request, 'home_page.html', context)
    else:
        raise Http404("Aucune forêt trouvée")
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





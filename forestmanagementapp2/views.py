import os
import random
from django.shortcuts import render, redirect
from .forms import PostFormIncident, PostFormOrganisme
from .models import ORGANISME


def randomImage():
    return [fichier for fichier in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/forest_pic')) if fichier.lower().endswith(('.jpeg'))]


def v_form_submitted(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    return render(request, 'formSubmitted.html', {'image_path': image_path})


def v_post_new_incident(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == "POST":
        incidentForm = PostFormIncident(request.POST)
        if incidentForm.is_valid():
            incidentPost = incidentForm.save(commit=False)
            incidentPost.statut_incident = "En cours"
            incidentPost.save(using='forestDB')
            return redirect('formSubmitted')
    else:
        incidentForm = PostFormIncident()
    return render(request, 'incidentForm.html', {
        'image_path': image_path,
        'title_page': "Formulaire d'incident",
        'title_form': "Décrivez l'incident",
        'description_form': "Veuillez décrire l'incident que vous avez vus, et indiquer le lieu en question.",
        'form': incidentForm,
    })


def v_register_new_species(request):
    objects = ORGANISME.objects.using('forestDB')
    print(objects)
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == "POST":
        speciesForm = PostFormOrganisme(request.POST)
        if speciesForm.is_valid():
            speciesForm.save(commit=True, using="forestDB")
            return redirect('formSubmitted')
    else:
        speciesForm = PostFormOrganisme()
    return render(request, 'incidentForm.html', {
        'image_path': image_path,
        'title_page': "Formulaire de nouvelle espèce",
        'title_form': "Détailler une nouvelle espèce dans une forêt.",
        'description_form': "Veuillez remplir les champs demandé tel que demandé dans le protocole.",
        'form': speciesForm,
    })

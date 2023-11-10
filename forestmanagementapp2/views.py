import os
import random
from django.shortcuts import render, redirect
from .forms import PostFormIncident, PostFormOrganism, ForestForm, OrganismForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import Foret, Organisme, Contient
from django.conf import settings



def home(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    return render(request, 'homePage.html', {'image_path': image_path})


def enter_forest(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    forets = Foret.objects.all()
    foret = None

    if request.method == 'POST':
        form = ForestForm(request.POST)
        if form.is_valid():
            foretclean = form.cleaned_data['nom_foret']
            try:
                foret = Foret.objects.get(nom_foret=foretclean)
                return redirect('home_page', nom_foret=foret)
            except Foret.DoesNotExist:
                foret = None
    else:
        form = ForestForm()
    return render(request, 'enter_forest.html', {'foret': form, 'forets': forets, 'image_path': image_path, 'foret_result': foret})


def home_page(request, nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    foret = Foret.objects.get(nom_foret=nom_foret)
    description = foret.get_description()
    return render(request, 'oneForestSelected.html', {'nom_foret': nom_foret, 'image_path': image_path, 'description': description})


def connexion(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger vers la page de tableau de bord après connexion
            return HttpResponseRedirect('/tableau_de_bord/')
        else:
            return render(request, 'connexion.html', {'error_message': 'Nom d\'utilisateur ou mot de passe incorrect'})
    else:
        return render(request, 'login.html', {'image_path': image_path})


def randomImage():
    return [fichier for fichier in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/forest_pic')) if fichier.lower().endswith(('.jpeg'))]


def v_form_submitted(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    return render(request, 'formSubmitted.html', {'image_path': image_path})


def v_post_new_incident(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == "POST":
        form = PostFormIncident(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.statut_incident = "En cours"
            post.save()
            return redirect('formSubmitted')
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
            post.save()
            return redirect('formSubmitted')
    else:
        form = PostFormOrganism()
    return render(request, 'incidentForm.html', {
        'image_path': image_path,
        'title_page': "Formulaire de nouvelle espèce",
        'title_form': "Détailler une nouvelle espèce dans une forêt.",
        'description_form': "Veuillez remplir les champs demandé tel que demandé dans le protocole.",
        'form': form,
    })


def organism_info(request,nom_organisme,nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    organisme=Organisme.objects.filter(nom_organisme=nom_organisme)
    organisme=list(organisme)
    description=organisme[0].description
    id_organisme=organisme[0].id_organisme

    return render(request, 'info_organism.html', {'image_path': image_path, 'oneSpecies':nom_organisme, 'nom_foret':nom_foret, 'description':description})


def v_list_of_species(request, nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    forest = Foret.objects.get(nom_foret=nom_foret)
    #Je récupère l'id_foret correspondant car dans la table contient j'en ai besoin
    id_forest = forest.pk
    print(id_forest)
    #Je récupère dans la table contient les id_organismes qui correpondent à mon id_foret
    contient_entries = Contient.objects.filter(id_foret=id_forest).values_list('id_organisme', flat=True)

    # Je transforme le QuerySet en une liste Python qui contient la liste de mes id_foret
    id_organismes = list(contient_entries)


    # Je cherche les noms d'organismes associés aux id de ma liste id_organismes
    organismes= Organisme.objects.filter(id_organisme__in=id_organismes).values_list('nom_organisme', flat=True)
    list_organismes=list(organismes)


    return render(request, "listOfSpecies.html", {
        'image_path': image_path,
        'nom_foret': nom_foret,
        'species':list_organismes
    })

def pictures(request, nom_foret):
    image_list=os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"static/{nom_foret}"))

    print('image_list:',image_list)
    return render(request, 'Pictures.html', {'image_list': image_list, 'nom_foret': nom_foret})

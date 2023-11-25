import os
import random
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import PostFormIncident, PostFormOrganism, ForestForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Foret, Organisme, Contient, Garde, Mission



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
                return redirect('forestSelected', nom_foret=foret)
            except Foret.DoesNotExist:
                foret = None
    else:
        form = ForestForm()
    return render(request, 'enter_forest.html', {
        'foret': form, 
        'forets': forets, 
        'image_path': image_path, 
        'foret_result': foret
        })


def forestSelected(request, nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    foret = Foret.objects.get(nom_foret=nom_foret)
    garde = Garde.objects.get(id_foret=foret.id_foret)
    description = foret.get_description()
    tel_garde=garde.num_telephone
    mail_garde=garde.mail_garde
    return render(request, 'oneForestSelected.html', {
        'nom_foret': nom_foret, 
        'image_path': image_path, 
        'description': description, 
        'latitude': foret.latitude, 
        'longitude': foret.longitude,
        'id_garde': garde.id_garde,
        'tel_garde': tel_garde,
        'mail_garde':mail_garde
        })


def connexion(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == "POST":
            username = request.POST.get('username', False)
            password = request.POST.get('password', False)

            db_user = User.objects.filter(username=username, password=password).first()   
            
            if db_user.username == username and db_user.password == password:
                login(request, db_user)
                name_forest_guard = Garde.objects.get(id_garde=db_user.pk).id_foret
                return redirect('forestSelected', nom_foret=name_forest_guard)
            else:
                print("User not found")
    return render(request, 'login.html', {'image_path': image_path})

def deconnexion(request):
    logout(request)
    return redirect('home')


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
        'description_form': "Veuillez décrire l'incident que vous avez vu, et indiquer le lieu en question.",
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
    organisme=Organisme.objects.filter(nom_organisme=nom_organisme).first()
    nutrition=organisme.nutrition
    description=organisme.description
    id_organisme=organisme.id_organisme
    foret = Foret.objects.filter(nom_foret=nom_foret).first()

    id_foret=foret.id_foret
    contient_entry = Contient.objects.filter(id_foret=id_foret, id_organisme=id_organisme).first()

    nombre_organisme = contient_entry.nombre_organisme
    return render(request, 'info_organism.html', {
        'image_path': image_path, 
        'oneSpecies':nom_organisme, 
        'nom_foret':nom_foret, 
        'description':description, 
        'nombre_organisme':nombre_organisme, 
        'nutrition': nutrition
    })


def v_list_of_species(request, nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    forest = Foret.objects.get(nom_foret=nom_foret)
    #Je récupère l'id_foret correspondant car dans la table contient j'en ai besoin
    id_forest = forest.pk
    #Je récupère dans la table contient les id_organismes qui correpondent à mon id_foret
    contient_entries = Contient.objects.filter(id_foret=id_forest).values_list('id_organisme', flat=True)

    # Je transforme le QuerySet en une liste Python qui contient la liste de mes id_foret
    id_organismes = list(contient_entries)

    # Je cherche les noms d'organismes associés aux id de ma liste id_organismes
    organismes= Organisme.objects.filter(id_organisme__in=id_organismes).values_list('nom_organisme', 'type')
    faune_list = [org[0] for org in organismes if org[1] == 'Faune']
    flore_list = [org[0] for org in organismes if org[1] == 'Flore']


    return render(request, "listOfSpecies.html", {
        'image_path': image_path,
        'nom_foret': nom_foret,
        'faune_list':faune_list,
        'flore_list': flore_list
    })


def pictures(request, nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    image_list=os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"static/{nom_foret}"))
    return render(request, 'Pictures.html', {
        'image_list': image_list, 
        'nom_foret': nom_foret,
        'image_path':image_path
    })


def missions(request, id_garde,nom_foret):

    missions_list = Mission.objects.filter(id_garde=id_garde)
    print(missions_list)
    context = {
        'id_garde': id_garde,
        'missions_list': missions_list,
        'nom_foret':nom_foret,
        'image_path': f"/forest_pic/{random.choice(randomImage())}",
    }

    return render(request, 'missions.html', context)

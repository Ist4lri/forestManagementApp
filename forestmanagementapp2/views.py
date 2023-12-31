import os
import random
from django.shortcuts import render, redirect
from .forms import PostFormIncident, PostFormOrganism, ForestForm, OrganismForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Foret, Organisme, Contient, Garde, Mission, Incident



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
    try : 
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
    except Garde.DoesNotExist:
        description = foret.get_description()
        return render(request, 'oneForestSelected.html', {
            'nom_foret': nom_foret, 
            'image_path': image_path, 
            'description': description, 
            'latitude': foret.latitude, 
            'longitude': foret.longitude,
            'id_garde': 0,
            'tel_garde': "En cas de danger, contactez le 18.",
            'mail_garde':"Il n'y a pas de garde dans cette forêt."
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


def v_form_submitted(request,nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    return render(request, 'formSubmitted.html', {'image_path': image_path, 'nom_foret': nom_foret})


def v_post_new_incident(request,nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    forest = Foret.objects.get(nom_foret=nom_foret)
    id_foret = forest.pk
    if request.method == "POST":
        form = PostFormIncident(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.statut_incident = "En cours"
            post.id_foret =id_foret
            post.save()
            return redirect('formSubmitted' , {'nom_foret': nom_foret})
    else:
        form = PostFormIncident()
    return render(request, 'incidentForm.html', {
        'image_path': image_path,
        'title_page': "Formulaire d'incident",
        'description_form': "Veuillez décrire l'incident que vous avez vu, et indiquer le lieu en question : ",
        'form': form,
        'nom_foret':nom_foret
    })


def v_register_new_species(request, nom_foret):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == "POST":
        formOgra = PostFormOrganism(request.POST)
        if formOgra.is_valid():
            postOrga = formOgra.save(commit=False)
            postOrga.save()
            return redirect('formSubmitted')
    else:
        formOgra = PostFormOrganism()
    return render(request, 'incidentForm.html', {
        'image_path': image_path,
        'title_page': "Formulaire de nouvelle espèce",
        'title_form': "Détailler une nouvelle espèce dans une forêt.",
        'description_form': "Veuillez remplir les champs demandé tel que demandé dans le protocole.",
        'form': formOgra,
        'nom_foret' : nom_foret
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
    id_forest = forest.pk
    contient_entries = Contient.objects.filter(id_foret=id_forest).values_list('id_organisme', flat=True)
    id_organismes = list(contient_entries)
    organismes= Organisme.objects.filter(id_organisme__in=id_organismes).values_list('nom_organisme', 'type')
    faune_list = sorted([org[0] for org in organismes if org[1] == 'Faune'])
    flore_list = sorted([org[0] for org in organismes if org[1] == 'Flore'])


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


def update_mission_etat(request,nom_foret):
    forest = Foret.objects.get(nom_foret=nom_foret)
    id_foret = forest.pk
    garde=Garde.objects.get(id_foret=id_foret)
    id_garde=garde.id_garde
    missions_list = Mission.objects.filter(id_garde=id_garde)
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == 'POST':
        missions_to_update = request.POST.getlist('mission')
        for mission_id in missions_to_update:
            mission = Mission.objects.get(pk=mission_id)
            mission.etat_mission = 'Terminé'
            mission.save()
    return render(request, 'missions.html', {'image_path':image_path, 'id_foret':id_foret, 'missions_list': missions_list, 'nom_foret':nom_foret})


def incidents(request, nom_foret):
    forest = Foret.objects.get(nom_foret=nom_foret)
    id_foret = forest.pk
    incidents_list=Incident.objects.filter(id_foret=id_foret)

    image_path = f"/forest_pic/{random.choice(randomImage())}"
    return render(request, 'incidents.html', {'image_path':image_path, 'id_foret':id_foret, 'incidents_list': incidents_list, 'nom_foret':nom_foret})

def update_incident_status(request,nom_foret):
    forest = Foret.objects.get(nom_foret=nom_foret)
    id_foret = forest.pk
    incidents_list = Incident.objects.filter(id_foret=id_foret)

    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == 'POST':
        incidents_to_update = request.POST.getlist('incidents')
        for incident_id in incidents_to_update:
            incident = Incident.objects.get(pk=incident_id)
            incident.statut_incident = 'Terminé'
            incident.save()
    return render(request, 'incidents.html', {'image_path':image_path, 'id_foret':id_foret, 'incidents_list': incidents_list, 'nom_foret':nom_foret})
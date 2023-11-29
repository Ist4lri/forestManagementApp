"""
URL configuration for forestManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from forestmanagementapp2.views import v_post_new_incident, v_form_submitted, v_register_new_species, enter_forest, forestSelected, connexion, organism_info, v_list_of_species, home,pictures, deconnexion, missions, incidents ,update_incident_status, update_mission_etat


urlpatterns = [
    path('admin/', admin.site.urls),
    path('choixforet/', enter_forest, name="enter_forest"),
    path('forestselected/<str:nom_foret>/', forestSelected, name='forestSelected'),
    path('forestselected/<str:nom_foret>/incidentForm/', v_post_new_incident, name="incident_form"),
    path('forestselected/<str:nom_foret>/formSubmitted/', v_form_submitted, name='formSubmitted'),
    path('registerSpecies/<str:nom_foret>', v_register_new_species, name='register_species'),
    path('listOfSpecies/<str:nom_foret>/', v_list_of_species, name="list_species"),
    path('login/', connexion, name='connexion'),
    path('listOfSpecies/<str:nom_foret>/info_org/<str:nom_organisme>/', organism_info, name='organism_info'),
    path('', home, name='home'),
    path('forestselected/<str:nom_foret>/pictures', pictures, name='pictures'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('<str:nom_foret>/<int:id_garde>/missions/', missions, name='missions'),
    path('<str:nom_foret>/incidents/', incidents, name='incidents'),
    path('<str:nom_foret>/update_incident_status/', update_incident_status, name='update_incident_status'),
    path('<str:nom_foret>/update_mission_etat/', update_mission_etat, name='update_mission_etat')

]
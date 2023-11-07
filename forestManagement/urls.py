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

from forestmanagementapp2.views import v_post_new_incident, v_form_submitted, v_register_new_species, enter_forest, home_page, connexion, organism_info, v_list_of_species


urlpatterns = [
    path('admin/', admin.site.urls),
    path('choixforet/', enter_forest, name="enter_forest"),
    path('accueil/<str:nom_foret>/', home_page, name='home_page'),
    path('incidentForm/', v_post_new_incident, name="incident_form"),
    path('formSubmitted/', v_form_submitted, name='formSubmitted'),
    path('registerSpecies/', v_register_new_species, name='register_species'),
    path('listOfSpecies/<str:nom_foret>/', v_list_of_species, name="list_species"),
    path('login/', connexion, name='connexion'),
    path('listOfSpecies/<str:nom_foret>/info_org/<str:nom_organisme>/', organism_info, name='organism_info')

]

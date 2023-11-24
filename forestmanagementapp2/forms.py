from django import forms
from .models import Incident,Organisme,Foret,Contient

class PostFormIncident(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ('description_incident',)


class PostFormOrganism(forms.ModelForm):

    class Meta:
        model = Organisme
        fields = ('nom_organisme', 'nutrition',
                  'facteur_emission', 'quantite_consommee_CO2', 'description', 'type')



class ForestForm(forms.ModelForm):
    class Meta:
        model = Foret
        fields = ('nom_foret','description','latitude','superficie','composition_sol','quantite_eau', 'id_foret', 'longitude')


class OrganismForm(forms.ModelForm):
    class Meta:
        model=Contient
        fields=('id_foret', 'id_organisme', 'nombre_organisme')
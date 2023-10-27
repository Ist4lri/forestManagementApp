from django import forms

from .models import INCIDENT, ORGANISM, FORET


class PostFormIncident(forms.ModelForm):

    class Meta:
        model = INCIDENT
        fields = ('description_incident',)


class PostFormOrganism(forms.ModelForm):

    class Meta:
        model = ORGANISM
        fields = ('nom_organisme', 'nutrition',
                  'facteur_emission', 'quantite_consommee_CO2')



class ForestForm(forms.ModelForm):
    class Meta:
        model = FORET
        fields = ['nom_foret']
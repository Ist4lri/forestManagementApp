from django import forms

from .models import Incident,Organisme,Foret


class PostFormIncident(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ('description_incident',)


class PostFormOrganism(forms.ModelForm):

    class Meta:
        model = Organisme
        fields = ('nom_organisme', 'nutrition',
                  'facteur_emission', 'quantite_consommee_CO2')



class ForestForm(forms.ModelForm):
    class Meta:
        model = Foret
        fields = ['nom_foret']
from django import forms

from .models import IncidentFormPost


class PostFormIncident(forms.ModelForm):

    class Meta:
        model = IncidentFormPost
        fields = ('description_incident',)

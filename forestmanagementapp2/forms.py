from django import forms

from .models import INCIDENT


class PostFormIncident(forms.ModelForm):

    class Meta:
        model = INCIDENT
        fields = ('description_incident',)

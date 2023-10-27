from django import forms


from .models import INCIDENT
from .models import ORGANISME


class PostFormIncident(forms.ModelForm):

    class Meta:
        model = INCIDENT
        fields = ('description_incident',)


class PostFormOrganisme(forms.ModelForm):

    class Meta:
        model = ORGANISME
        fields = '__all__'

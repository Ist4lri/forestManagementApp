from django import forms
from forestmanagementapp2.models import FORET

class ForetForm(forms.ModelForm):
    class Meta:
        model = FORET
        fields = ['nom_foret']
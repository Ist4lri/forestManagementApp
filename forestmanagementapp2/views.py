from django.shortcuts import render
from .forms import PostFormIncident


def v_post_new_incident(request):
    form = PostFormIncident()
    return render(request, 'incidentForm.html', {'form': form})

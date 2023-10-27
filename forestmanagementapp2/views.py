from django.shortcuts import render, redirect
from .forms import PostFormIncident


def v_form_submitted(request):
    return render(request, 'formSubmitted.html')


def v_post_new_incident(request):
    if request.method == "POST":
        form = PostFormIncident(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.statut_incident = "En cours"
            post.save(using='forestDB')
            return redirect('formSubmitted')
    else:
        form = PostFormIncident()
    return render(request, 'incidentForm.html', {'form': form})

import os
import random
from django.shortcuts import render, redirect
from .forms import PostFormIncident


def randomImage():
    return [fichier for fichier in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/forest_pic')) if fichier.lower().endswith(('.jpeg'))]


def v_form_submitted(request, image_path="/forest_pic/for1.jpeg"):
    return render(request, 'formSubmitted.html', {'image_path': image_path})


def v_post_new_incident(request):
    image_path = f"/forest_pic/{random.choice(randomImage())}"
    if request.method == "POST":
        form = PostFormIncident(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.statut_incident = "En cours"
            post.save(using='forestDB')
            return redirect('formSubmitted', image_path)
    else:
        form = PostFormIncident()
    return render(request, 'incidentForm.html', {'form': form, 'image_path': image_path})

from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        choix = request.POST.get('choix', '')  # Récupérer la valeur sélectionnée dans le menu déroulant
        # Effectuez ici le traitement en fonction du choix
    return render(request, 'home.html')
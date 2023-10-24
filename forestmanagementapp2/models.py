from django.db import models


class FORET(models.Model):
    nom_foret = models.CharField(max_length=500, unique=True, primary_key=True)
    localisation = models.CharField(max_length=100)
    densite = models.IntegerField()
    superfice = models.IntegerField()
    quantite_eau = models.IntegerField()
    composition_sol = models.TextField()


class ORGANISM(models.Model):
    nom_organisme = models.CharField(
        max_length=500, unique=True, primary_key=True)
    nutrition = models.CharField(max_length=300)
    facteur_emission = models.IntegerField()
    quantite_consomméé_CO2 = models.IntegerField()


class GARDE(models.Model):
    id_garde = models.IntegerField(primary_key=True)
    nom_foret = models.ForeignKey(
        FORET, on_delete=models.CASCADE)
    nom_garde = models.CharField(max_length=50)
    prenom_garde = models.CharField(max_length=50)


class CONTIENT(models.Model):
    nom_foret = models.ForeignKey(
        FORET, on_delete=models.CASCADE, primary_key=True)
    nom_organisme = models.ForeignKey(
        ORGANISM, on_delete=models.CASCADE)
    nombre_organisme = models.IntegerField()


class IncidentFormPost(models.Model):
    id_incident = models.IntegerField(primary_key=True)
    description_incident = models.TextField()
    statut_incident = models.CharField(max_length=200)

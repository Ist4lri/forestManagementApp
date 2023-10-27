from django.db import models


class FORET(models.Model):
    nom_foret = models.TextField(primary_key=True)
    localisation = models.TextField()
    densite = models.IntegerField()
    superfice = models.IntegerField()
    quantite_eau = models.IntegerField()
    composition_sol = models.TextField()

    class Meta:
        managed = False

        db_table = 'FORET'



class ORGANISM(models.Model):
    nom_organisme = models.TextField(primary_key=True)
    nutrition = models.TextField()
    facteur_emission = models.IntegerField()

    quantite_consommee_CO2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ORGANISM'
   



class GARDE(models.Model):
    id_garde = models.IntegerField(primary_key=True)
    nom_foret = models.ForeignKey(
        FORET, on_delete=models.CASCADE)
    nom_garde = models.TextField()
    prenom_garde = models.TextField()
    adresse_garde = models.TextField()
    num_telephone = models.TextField()
    mail_garde = models.TextField()
    date_embauche = models.TextField()

    class Meta:
        managed = False

        db_table = 'GARDE'



class INCIDENT(models.Model):
    id_incident = models.IntegerField(primary_key=True)
    description_incident = models.TextField()
    statut_incident = models.TextField()

    class Meta:
        managed = False
        db_table = 'INCIDENT'



class MISSION(models.Model):
    id_mission = models.IntegerField(primary_key=True)
    id_garde = models.ForeignKey(
        GARDE, on_delete=models.CASCADE)
    description_mission = models.TextField()
    etat_mission = models.TextField()

    class Meta:
        managed = False

        db_table = 'MISSION'

        


class CONTIENT(models.Model):
    nom_foret = models.ForeignKey(
        FORET, on_delete=models.CASCADE, primary_key=True)
    nom_organisme = models.ForeignKey(
        ORGANISM, on_delete=models.CASCADE)
    nombre_organisme = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CONTIENT'



class POSSEDE(models.Model):
    id_mission = models.ForeignKey(
        MISSION, on_delete=models.CASCADE)
    id_garde = models.ForeignKey(
        GARDE, on_delete=models.CASCADE, primary_key=True)
    date_mission = models.TextField()
    etat_mission = models.TextField()

    class Meta:
        managed = False

        db_table = 'POSSEDE'



class TOUCHE(models.Model):
    nom_foret = models.ForeignKey(
        FORET, on_delete=models.CASCADE)
    id_incident = models.ForeignKey(
        INCIDENT, on_delete=models.CASCADE, primary_key=True)
    date_incident = models.TextField()

    class Meta:
        managed = False

        db_table = 'TOUCHE'


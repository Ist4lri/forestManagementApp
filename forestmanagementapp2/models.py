from django.db import models
<<<<<<< HEAD
<<<<<<< HEAD
=======
from django.contrib.auth.models import AbstractUser
>>>>>>> 1187063 (new pic)
=======

>>>>>>> 11793b8 (try to do connexion view)

class Contient(models.Model):
    id_foret = models.OneToOneField(
        'Foret', models.DO_NOTHING, db_column='id_foret', primary_key=True)
    id_organisme = models.ForeignKey(
        'Organisme', models.DO_NOTHING, db_column='id_organisme')
    nombre_organisme = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CONTIENT'

    def get_list_organism(self):
        self.id_organisme


class Foret(models.Model):
    id_foret = models.AutoField(primary_key=True)
    nom_foret = models.TextField(blank=True)
    latitude = models.TextField(blank=True)
    densite = models.IntegerField(blank=True)
    superficie = models.IntegerField(blank=True)
    quantite_eau = models.IntegerField(blank=True)
    composition_sol = models.TextField(blank=True)
    description = models.TextField(blank=True)
    longitude = models.TextField(blank=True)

    def __str__(self):
        return self.nom_foret

    def get_description(self):
        return self.description


    class Meta:
        managed = False
        db_table = 'FORET'


<<<<<<< HEAD

class Garde(models.Model): #AbstractUser
=======
class Garde(AbstractUser):
>>>>>>> 1187063 (new pic)
    id_garde = models.AutoField(primary_key=True)
    id_foret = models.ForeignKey(
        Foret, models.DO_NOTHING, db_column='id_foret')
    nom_garde = models.TextField()
    prenom_garde = models.TextField()
    adresse_garde = models.TextField()
    num_telephone = models.TextField()
    mail_garde = models.TextField()
    date_embauche = models.TextField()

    class Meta:
        managed = False
        db_table = 'GARDE'


class Incident(models.Model):
    id_incident = models.AutoField(primary_key=True)
    description_incident = models.TextField()
    statut_incident = models.TextField()

    class Meta:
        managed = False
        db_table = 'INCIDENT'


class Mission(models.Model):
    id_mission = models.AutoField(primary_key=True)
    id_garde = models.ForeignKey(
        Garde, models.DO_NOTHING, db_column='id_garde')
    description_mission = models.TextField()
    etat_mission = models.TextField()

    class Meta:
        managed = False
        db_table = 'MISSION'


class Organisme(models.Model):
    id_organisme = models.AutoField(primary_key=True)
    nom_organisme = models.TextField()
    nutrition = models.TextField()
    facteur_emission = models.IntegerField()
    # Field name made lowercase.
    quantite_consommee_CO2 = models.IntegerField(
        db_column='quantite_consommee_CO2')
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'ORGANISME'


class Possede(models.Model):
    id_mission = models.OneToOneField(
        Mission, models.DO_NOTHING, db_column='id_mission', primary_key=True)
    id_garde = models.ForeignKey(
        Garde, models.DO_NOTHING, db_column='id_garde')
    date_mission = models.TextField()
    etat_mission = models.TextField()

    class Meta:
        managed = False
        db_table = 'POSSEDE'


class Touche(models.Model):
    id_foret = models.OneToOneField(
        Foret, models.DO_NOTHING, db_column='id_foret', primary_key=True)
    id_incident = models.ForeignKey(
        Incident, models.DO_NOTHING, db_column='id_incident')
    date_incident = models.TextField()

    class Meta:
        managed = False
        db_table = 'TOUCHE'
<<<<<<< HEAD

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'
<<<<<<< HEAD
=======

>>>>>>> 11793b8 (try to do connexion view)
=======
>>>>>>> b2171e6 (login)

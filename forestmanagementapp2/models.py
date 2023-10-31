from django.db import models


class Contient(models.Model):
    id_foret = models.OneToOneField(
        'Foret', models.DO_NOTHING, db_column='id_foret', primary_key=True)
    id_organisme = models.ForeignKey(
        'Organisme', models.DO_NOTHING, db_column='id_organisme')
    nombre_organisme = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CONTIENT'


class Foret(models.Model):
    id_foret = models.AutoField(primary_key=True)
    nom_foret = models.TextField()
    localisation = models.TextField()
    densite = models.IntegerField()
    superficie = models.IntegerField()
    quantite_eau = models.IntegerField()
    composition_sol = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.nom_foret

    def get_description(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'FORET'


class Garde(models.Model):
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

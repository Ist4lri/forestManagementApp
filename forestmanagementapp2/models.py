from django.db import models


class CONTIENT(models.Model):
    # The composite primary key (nom_foret, nom_organisme) found, that is not supported. The first column is selected.
    nom_foret = models.OneToOneField(
        'Foret', models.DO_NOTHING, db_column='nom_foret', primary_key=True, blank=True)
    nom_organisme = models.ForeignKey(
        'Organisme', models.DO_NOTHING, db_column='nom_organisme', blank=True)
    nombre_organisme = models.IntegerField(blank=True)

    class Meta:
        managed = False
        db_table = 'CONTIENT'


class FORET(models.Model):
    nom_foret = models.TextField(primary_key=True, blank=True)
    localisation = models.TextField(blank=True)
    densite = models.IntegerField(blank=True)
    superficie = models.IntegerField(blank=True)
    quantite_eau = models.IntegerField(blank=True)
    composition_sol = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'FORET'


class GARDE(models.Model):
    id_garde = models.AutoField(primary_key=True, blank=True)
    nom_foret = models.ForeignKey(
        FORET, models.DO_NOTHING, db_column='nom_foret', to_field=None, blank=True)
    nom_garde = models.TextField(blank=True)
    prenom_garde = models.TextField(blank=True)
    adresse_garde = models.TextField(blank=True)
    num_telephone = models.TextField(blank=True)
    mail_garde = models.TextField(blank=True)
    date_embauche = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'GARDE'


class INCIDENT(models.Model):
    id_incident = models.AutoField(primary_key=True, blank=True)
    description_incident = models.TextField(blank=True)
    statut_incident = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'INCIDENT'


class MISSION(models.Model):
    # The composite primary key (id_mission, id_garde) found, that is not supported. The first column is selected.
    id_mission = models.AutoField(primary_key=True, blank=True)
    id_garde = models.OneToOneField(
        GARDE, models.DO_NOTHING, db_column='id_garde', blank=True)
    description_mission = models.TextField(blank=True)
    etat_mission = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'MISSION'


class ORGANISME(models.Model):
    nom_organisme = models.TextField(primary_key=True, blank=True)
    nutrition = models.TextField(blank=True)
    facteur_emission = models.IntegerField(blank=True)
    # Field name made lowercase.
    quantite_consommee_co2 = models.IntegerField(
        db_column='quantite_consommee_CO2', blank=True)

    class Meta:
        managed = False
        db_table = 'ORGANISME'


class POSSEDE(models.Model):
    # The composite primary key (id_mission, id_garde) found, that is not supported. The first column is selected.
    id_mission = models.OneToOneField(
        MISSION, models.DO_NOTHING, db_column='id_mission', primary_key=True, blank=True)
    id_garde = models.ForeignKey(
        GARDE, models.DO_NOTHING, db_column='id_garde', blank=True)
    date_mission = models.TextField(blank=True)
    etat_mission = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'POSSEDE'


class TOUCHE(models.Model):
    # The composite primary key (nom_foret, id_incident) found, that is not supported. The first column is selected.
    nom_foret = models.OneToOneField(
        FORET, models.DO_NOTHING, db_column='nom_foret', primary_key=True, blank=True)
    id_incident = models.ForeignKey(
        INCIDENT, models.DO_NOTHING, db_column='id_incident', blank=True)
    date_incident = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'TOUCHE'

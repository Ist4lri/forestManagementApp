
from django.db import migrations,models


class Contient(models.Model):
    id_foret = models.OneToOneField('Foret', models.DO_NOTHING, db_column='id_foret', primary_key=True, blank=True   )
    id_organisme = models.ForeignKey('Organisme', models.DO_NOTHING, db_column='id_organisme', blank=True   )
    nombre_organisme = models.IntegerField(blank=True   )

    class Meta:
        managed = False
        db_table = 'CONTIENT'


class Foret(models.Model):
    id_foret = models.AutoField(primary_key=True, blank=True   )
    nom_foret = models.TextField(blank=True   )
    localisation = models.TextField(blank=True   )
    densite = models.IntegerField(blank=True   )
    superficie = models.IntegerField(blank=True   )
    quantite_eau = models.IntegerField(blank=True   )
    composition_sol = models.TextField(blank=True   )
    description = models.TextField(blank=True   )

    class Meta:
        managed = False
        db_table = 'FORET'


class Garde(models.Model):
    id_garde = models.AutoField(primary_key=True, blank=True   )
    id_foret = models.ForeignKey(Foret, models.DO_NOTHING, db_column='id_foret', blank=True   )
    nom_garde = models.TextField(blank=True   )
    prenom_garde = models.TextField(blank=True   )
    adresse_garde = models.TextField(blank=True   )
    num_telephone = models.TextField(blank=True   )
    mail_garde = models.TextField(blank=True   )
    date_embauche = models.TextField(blank=True   )

    class Meta:
        managed = False
        db_table = 'GARDE'


class Incident(models.Model):
    id_incident = models.AutoField(primary_key=True, blank=True   )
    description_incident = models.TextField(blank=True   )
    statut_incident = models.TextField(blank=True   )

    class Meta:
        managed = False
        db_table = 'INCIDENT'


class Mission(models.Model):
    id_mission = models.AutoField(primary_key=True, blank=True   )
    id_garde = models.ForeignKey(Garde, models.DO_NOTHING, db_column='id_garde', blank=True   )
    description_mission = models.TextField(blank=True   )
    etat_mission = models.TextField(blank=True   )

    class Meta:
        managed = False
        db_table = 'MISSION'


class Organisme(models.Model):
    id_organisme = models.AutoField(primary_key=True, blank=True   )
    nom_organisme = models.TextField(blank=True   )
    nutrition = models.TextField(blank=True   )
    facteur_emission = models.IntegerField(blank=True   )
    quantite_consommee_CO2 = models.IntegerField(db_column='quantite_consommee_CO2', blank=True   )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORGANISME'


class Possede(models.Model):
    id_mission = models.OneToOneField(Mission, models.DO_NOTHING, db_column='id_mission', primary_key=True, blank=True   )
    id_garde = models.ForeignKey(Garde, models.DO_NOTHING, db_column='id_garde', blank=True   )
    date_mission = models.TextField(blank=True   )
    etat_mission = models.TextField(blank=True   )

    class Meta:
        managed = False
        db_table = 'POSSEDE'


class Touche(models.Model):
    id_foret = models.OneToOneField(Foret, models.DO_NOTHING, db_column='id_foret', primary_key=True, blank=True   )
    id_incident = models.ForeignKey(Incident, models.DO_NOTHING, db_column='id_incident', blank=True   )
    date_incident = models.TextField(blank=True   )

    class Meta:
        managed = False
        db_table = 'TOUCHE'

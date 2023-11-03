# Generated by Django 4.1 on 2023-10-27 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FORET',
            fields=[
                ('nom_foret', models.TextField(primary_key=True, serialize=False)),
                ('localisation', models.TextField()),
                ('densite', models.IntegerField()),
                ('superfice', models.IntegerField()),
                ('quantite_eau', models.IntegerField()),
                ('composition_sol', models.TextField()),
            ],
            options={
                'db_table': 'FORET',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GARDE',
            fields=[
                ('id_garde', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_garde', models.TextField()),
                ('prenom_garde', models.TextField()),
                ('adresse_garde', models.TextField()),
                ('num_telephone', models.TextField()),
                ('mail_garde', models.TextField()),
                ('date_embauche', models.TextField()),
            ],
            options={
                'db_table': 'GARDE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='INCIDENT',
            fields=[
                ('id_incident', models.IntegerField(primary_key=True, serialize=False)),
                ('description_incident', models.TextField()),
                ('statut_incident', models.TextField()),
            ],
            options={
                'db_table': 'INCIDENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MISSION',
            fields=[
                ('id_mission', models.IntegerField(primary_key=True, serialize=False)),
                ('description_mission', models.TextField()),
                ('etat_mission', models.TextField()),
            ],
            options={
                'db_table': 'MISSION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ORGANISM',
            fields=[
                ('nom_organisme', models.TextField(primary_key=True, serialize=False)),
                ('nutrition', models.TextField()),
                ('facteur_emission', models.IntegerField()),
                ('quantite_consommee_CO2', models.IntegerField()),
            ],
            options={
                'db_table': 'ORGANISM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CONTIENT',
            fields=[
                ('nom_foret', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='forestmanagementapp2.foret')),
                ('nombre_organisme', models.IntegerField()),
            ],
            options={
                'db_table': 'CONTIENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='POSSEDE',
            fields=[
                ('id_garde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='forestmanagementapp2.garde')),
                ('date_mission', models.TextField()),
                ('etat_mission', models.TextField()),
            ],
            options={
                'db_table': 'POSSEDE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TOUCHE',
            fields=[
                ('id_incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='forestmanagementapp2.incident')),
                ('date_incident', models.TextField()),
            ],
            options={
                'db_table': 'TOUCHE',
                'managed': False,
            },
        ),
    ]
# Generated by Django 3.0.5 on 2020-08-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.FloatField(default=0.0)),
                ('wc', models.FloatField(default=0.0)),
                ('coarse_aggregate', models.FloatField(default=0.0)),
                ('fine_aggregate', models.FloatField(default=0.0)),
                ('blast_furance_slag', models.FloatField(default=0.0)),
                ('superplasticizer', models.FloatField(default=0.0)),
                ('age', models.FloatField(default=0.0)),
                ('compressive_strength', models.FloatField(default=0.0)),
            ],
        ),
    ]

# Generated by Django 3.0.5 on 2020-08-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concrete', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictmodel',
            name='age',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predictmodel',
            name='blast_furance_slag',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predictmodel',
            name='coarse_aggregate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predictmodel',
            name='compressive_strength',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predictmodel',
            name='fine_aggregate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predictmodel',
            name='superplasticizer',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predictmodel',
            name='water',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predictmodel',
            name='wc',
            field=models.FloatField(),
        ),
    ]

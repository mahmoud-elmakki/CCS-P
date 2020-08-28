from django.db import models


class PredictModel(models.Model):
	
	water = models.FloatField()
	wc = models.FloatField()
	coarse_aggregate = models.FloatField()
	fine_aggregate = models.FloatField()
	blast_furance_slag = models.FloatField()
	superplasticizer = models.FloatField()
	age = models.FloatField()
	compressive_strength = models.FloatField(default=0.0)

	def __str__(self):
		return self.wc




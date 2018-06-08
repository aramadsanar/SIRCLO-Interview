from django.db import models

DATE_INPUT_FORMATS = ['%d-%m-%Y']

# Create your models here.
class WeightEntry(models.Model):
	data_date = models.DateField(auto_now_add=True)
	min_weight = models.IntegerField(default=0)
	max_weight = models.IntegerField(default=0)
	variance = models.IntegerField(default=0)






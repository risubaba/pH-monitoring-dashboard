from django.db import models
from django.utils  import timezone


class MainModel(models.Model):
	pH_value = models.DecimalField(decimal_places=2,max_digits=4, default=7)


	def __str__(self):
		return str(self.pk)

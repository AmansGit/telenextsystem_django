from django.db import models

# Create your models here.


class Registration(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=100)
	email = models.EmailField(max_length=50	)
	password = models.CharField(max_length=100)

	class Meta:
		db_table = 'registration'

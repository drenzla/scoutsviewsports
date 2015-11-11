from django.db import models

# Create your models here.
class AthlUser(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length= 30)
	level = models.CharField(max_length=20)
	school = models.CharField(max_length=50)
	coach = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	birthdate = models.CharField(max_length=10)

class FanUser(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length= 30)
	address = models.CharField(max_length=100)
	group = models.CharField(max_length=30)
	birthdate = models.CharField(max_length=10)

class CoachUser(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length= 30)
	level = models.CharField(max_length=20)
	school = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	birthdate = models.CharField(max_length=10)

from django.db import models

# Create your models here.
class Registrations(models.Model):
	Name = models.CharField(max_length=30)
	PhNo = models.IntegerField()
	EMail = models.EmailField(max_length=30)
	Address = models.TextField()
	PassWord = models.TextField()

class Info(models.Model):
	Name = models.CharField(max_length=30)
	Material = models.CharField(max_length=30)
	Quantity = models.TextField()
	PhNo = models.IntegerField()
	EMail = models.EmailField()
	Address = models.TextField()
	Value = models.IntegerField()
	Type = models.CharField(max_length=30)
	Status = models.CharField(max_length=20)

class Admin(models.Model):
	Name = models.CharField(max_length=30)
	PassWord = models.TextField()
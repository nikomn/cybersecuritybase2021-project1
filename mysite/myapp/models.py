from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Patron(models.Model):
  username = models.TextField()
  password = models.TextField()
  ssn = models.TextField(max_length=140, default='')
  firstname = models.TextField(max_length=140, default='')
  lastname = models.TextField(max_length=140, default='')
  address = models.TextField(max_length=140, default='No address')
  logged = models.TextField(default='False')

class PhoneNumber(models.Model):
  owner = models.ForeignKey(Patron, on_delete=models.CASCADE)
  number = models.TextField()
  information = models.TextField()
  def __str__(self):
    return self.number


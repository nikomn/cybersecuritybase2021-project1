from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
  username = models.TextField()
  password = models.TextField()

class Account(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  uid = models.TextField()
  def __str__(self):
    return self.uid


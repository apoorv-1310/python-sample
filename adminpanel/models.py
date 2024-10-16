from django.db import models

# Create your models here.

class GymOwners(models.Model):
    "_id" =  models.CharField(max_length=30)
    "fname" =  models.CharField(max_length=30)
    "lname" = models.CharField(max_length=30)
    "phoneNo" = models.CharField(max_length=30)
    "email" = models.CharField(max_length=30)
    "password" = models.CharField(max_length=30)
    "createdOn" = models.DateField()
    "updatedOn" = models.DateField()

    class Meta:
        db_table = 'gym_owners'
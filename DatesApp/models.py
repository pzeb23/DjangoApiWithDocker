from django.db import models

# Create your models here.

class Dates(models.Model):
    Id = models.AutoField(primary_key = True)
    Month = models.CharField(max_length=12)
    Day = models.IntegerField()
    Fact = models.CharField(max_length=500)

class Months(models.Model):
    Id = models.AutoField(primary_key = True)
    Month = models.CharField(max_length=12)
    DaysChecked = models.IntegerField()
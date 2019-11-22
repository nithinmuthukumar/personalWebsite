from django.db import models
from .fields import IntegerRangeField
import datetime
from django.utils import timezone

class Achievement(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Project(models.Model):
    date=models.DateField()
    name=models.CharField(max_length=30)
    link=models.URLField()
class Skill(models.Model):
    info=models.CharField(max_length=30)

class Club(models.Model):
    name=models.CharField(max_length=30)
    duration=models.DurationField()
#need a certifications model















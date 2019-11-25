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
    img=models.ImageField()


class Skill(models.Model):
    info=models.CharField(max_length=30)


class Interest(models.Model):
    info=models.CharField(max_length=30)


class Club(models.Model):
    name=models.CharField(max_length=30)
    duration=models.DurationField()


class School(models.Model):
    name=models.CharField(max_length=30)

class Experience(models.Model):
    hours=models.IntegerField()
    info=models.CharField(max_length=100)



# need a certifications model

# also need to look at model relationship thingy by reviewing model documentation in django















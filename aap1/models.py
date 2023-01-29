from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=55, null=True)
    rollno  = models.IntegerField(max_length=55, null=True)
    phone = models.CharField(max_length=13, null=True)

class Games(models.Model):
    gamename = models.CharField(max_length=50, null=True)
    point = models.IntegerField(max_length=100, null=True)



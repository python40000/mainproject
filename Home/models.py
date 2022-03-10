from django.db import models

# Create your models here.

class Faculty(models.Model):
    faculty_id = models.IntegerField()
    faculty_name = models.CharField(max_length=30)
    faculty_place = models.CharField(max_length=30)
    faculty_position = models.CharField(max_length=40)
    faculty_email = models.CharField(max_length=40)
    faculty_password = models.CharField(max_length=40)

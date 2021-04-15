from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Student Model
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20)
    def _str_(self):
        return self.user.username


# Recruiter Model
class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20)
    company = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    def _str_(self):
        return self.user.username


# Job Model
class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=20,null=True)
    location = models.CharField(max_length=30,null=True)
    experience = models.CharField(max_length=30,null=True)
    salary = models.CharField(max_length=20,null=True)
    description = models.CharField(max_length=100,null=True)
    
    def _str_(self):
        return self.title 
     

from django.db import models
from django.contrib.auth.models import AbstractUser


import time
from datetime import datetime

from users.models import User
from django.utils import timezone

class Course(models.Model):
    name = models.CharField(max_length  = 255)
    description = models.TextField(max_length =1000, null = True, blank = True)
    participants = models.ManyToManyField(User , blank = True, related_name = "events")
    start_date = models.DateTimeField(null = True, blank = True)
    end_date = models.DateTimeField(null = True, blank = True)
    created = models.DateField(auto_now_add = True) #Create 
    updated  = models.DateField(auto_now = True) #Update

    def __str__ (self):
        return self.name
    
    class Meta:
        ordering = ['-end_date']

    @property
    def course_status(self):
        present = timezone.now()

        if self.start_date <= present <= self.end_date:
            status = 'Ongoing'
        elif present > self.end_date:
            status = 'Finished'
        else:
            status = 'Upcoming'

        return status



class Assignements(models.Model):
    Title = models.CharField(max_length=200 , null = True)
    Details = models.TextField(max_length=8000, null = True,blank=True)
    created = models.DateField(auto_now_add = True) #Create 
    end_date = models.DateTimeField(null = True, blank = True)
    Documents = models.FileField(upload_to='./documents/',null = True, blank = True)     
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="AssCourse") 
    def __str__(self):
        return  f"{self.course.name} + {self.Title}"
    class Meta:
        ordering = ['-created']
    @property
    def status(self):
        present = timezone.now()

        if  present <= self.end_date:
            status = 'Ongoing'
        elif present > self.end_date:
            status = 'Finished'
        else:
            status = 'Upcoming'

        return status
    
    class Meta:
        ordering = ['-created']

class Submission(models.Model):
    participant = models.ForeignKey(User, on_delete = models.SET_NULL , null = True , related_name="submission")
    Course = models.ForeignKey(Course, on_delete = models.SET_NULL, null = True)
    details = models.CharField(max_length =400, null = True, blank = True)
    Assignement = models.ForeignKey(Assignements, on_delete = models.CASCADE, null = True, related_name="subAssignement")
    Document = models.FileField(upload_to='./submissions/',null = True, blank = True)     
    created = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    # Mark = models.FloatField(null = True , blank=True)
    
    def __str__(self):
        return str(self.participant.name) + '-----' + str(self.Course)

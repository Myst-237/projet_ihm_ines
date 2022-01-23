from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


User = settings.AUTH_USER_MODEL
# Create your models here.
Roles = [
    ('NoRole', 'NoRole'),
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
    ('Receptionist', 'Receptionist'),
    ('Admin', 'Admin'),
    ('Accountant', 'Accountant'),
    ('Nurse', 'Nurse'),
    ('Labtech', 'Labtech'),
    ('HRM', 'HRM'),
    ('Specialist', 'Specialist'),
]

Departments = [
    ('MG', 'Medicine General'),
    ('CA', 'Cardiologie'),
    ('CH', 'Chirurgi'),
    ('MA', 'Maternite'),
    ('UR', 'Urgence'),
    ('RA', 'Radiologie'),
    ('PE', 'Pediatrie')
]

Gender = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

#creating the different specialities for specialist doctors
Speciality = [
    ('NoSpeciality', 'NoSpeciality'),
    ('Dermatology', 'Dermatology'),
    ('Radiology', 'Radiology'),
]

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, default='NoRole', choices = Roles)
    
    def __str__(self):
        return self.username 

class Department(models.Model):
    name = models.CharField(max_length=100, choices = Departments)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
#patient model   
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    place_of_birth = models.CharField(max_length=200)
    person_to_contact = models.CharField(max_length=100)
    person_to_contact_tel = models.CharField(max_length=100)
    age  = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices = Gender)
    tel = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=250, blank = True, null = True)
    date_of_birth = models.DateField(blank = True, null = True)
    profession = models.CharField(max_length=100, blank = True, null = True)
    profile_pic = models.ImageField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        
        return super(Patient, self).save(*args, **kwargs)
    
#doctor model   
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    specialist = models.BooleanField(default=False)
    speciality =  models.CharField(max_length=100, default='NoSpeciality', choices = Speciality)
    
    def __str__(self):
        return self.user.username
    
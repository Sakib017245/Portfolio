from django.db import models
from django.contrib.auth.models import *
from django_resized import ResizedImageField

# Create your models here.

class About(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    description = models.TextField(blank=True,null=True)
    short_description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return str(self.user)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    birthday = models.DateField(blank=True,null=True,default=None)
    website = models.CharField(blank=True, null=True, max_length=250 , default= None)
    phone = models.CharField(blank=True, null=True, max_length=250)
    city = models.CharField(blank=True, null=True, max_length=250)
    age = models.IntegerField(blank=True, null=True)
    degree = models.CharField(blank=True, null=True, max_length=250)
    email = models.CharField(blank=True, null=True, max_length=250)
    profile_image = ResizedImageField(blank=True, null=True, size=[500, 300], quality=75, upload_to='img')

    def __str__(self):
        return str(self.user)

class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    skill_level = models.IntegerField()
    
    def __str__(self):
        return str(self.user)

class Summary(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    phone = models.CharField(blank=True, null=True, max_length=250)
    email = models.CharField(blank=True, null=True, max_length=250)

    def __str__(self):
        return str(self.user)


class Education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    degree = models.CharField(max_length=250)
    institute = models.CharField(blank=True,null=True,max_length=250,default=None)
    result = models.CharField(blank=True,null=True,max_length=250,default=None)
    start_date = models.DateField(blank=True,null=True,default=None)
    end_date = models.DateField(blank=True,null=True,default=None)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.user)

class ProfessionaExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sector = models.CharField(max_length=250,blank=True,null=True, default=None)
    institute = models.CharField(blank=True,null=True,max_length=250)
    start_date = models.DateField(blank=True,null=True,default=None)
    end_date = models.DateField(blank=True,null=True,default=None)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.user)

class Service(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service_name = models.CharField(max_length=250)
    service_details = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.user)

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project_image = ResizedImageField(blank=True, null=True, size=[500, 300],  crop=['top', 'left'], quality=75, upload_to='img')
    project_title = models.CharField(max_length=250)
    project_description = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.user)


from django.db import models
from ThoughtXplore.txUser.models import User
from ThoughtXplore.txMisc.models import StateContentType
# Create your models here.

class UserContact(models.Model):
    User = models.ForeignKey(User)
    SCI = models.ForeignKey(StateContentType)
    Mobileno = models.CharField(max_length=15)
    Phoneno = models.CharField(max_length=15)
    AltEmailAdress = models.CharField(max_length=500)
    
    Father_FirstName = models.CharField(max_length=500)
    Father_MiddleName = models.CharField(max_length=500)
    Father_LastName = models.CharField(max_length=500)
    FatherContactNo = models.CharField(max_length=15)
    
    MotherName = models.CharField(max_length=500)
    Mother_FirstName = models.CharField(max_length=500)
    Mother_MiddleName = models.CharField(max_length=500)
    Mother_LastName = models.CharField(max_length=500)
    MotherContactNo = models.CharField(max_length=15)


class ContactAdress(models.Model):
    Lane1 = models.CharField(max_length=1000)
    Lane2 = models.CharField(max_length=1000)
    City = models.CharField(max_length=1000)
    Province = models.CharField(max_length=1000)
    State = models.CharField(max_length=1000)
    PostalCode = models.CharField(max_length=1000)
    
class UserContactAdress(models.Model):
    User = models.ForeignKey(User)
    ContactAdress = models.ForeignKey(ContactAdress)
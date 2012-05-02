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
    FatherName = models.CharField(max_length=500)
    FatherContactNo = models.CharField(max_length=15)
    MotherName = models.CharField(max_length=500)
    MotherContactNo = models.CharField(max_length=15)
    AlternateAdress = models.CharField(max_length=1000)
    Adress = models.CharField(max_length=1000)
    
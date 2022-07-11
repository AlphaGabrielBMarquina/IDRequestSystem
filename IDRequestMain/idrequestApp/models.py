from random import choices
from turtle import width
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Useraccount(AbstractUser):

    Usertype = [
        ('A', 'Admin'),
        ('S', 'Student'),
        ('F', 'Faculty'),]

    Usertype = models.CharField(choices = Usertype, max_length = 10, verbose_name = 'Usertype', default='S') 


    


class registration(models.Model):
    crs =[('BSCE','(BSCE) BS - Civil Engineering'),
    ('BSEE','(BSEE) BS - Electrical Engineering'),
    ('BSME','(BSME) BS - Mechanical Engineering'),
    ('BET - CPET','(BET - CPET) BET - Computer Engineering Technology'),
    ('BET - CT','(BET - CT) BET - Construction Technology'),
    ('BET - ET','(BET - ET) BET - Electrical Technology'),
    ('BET - ESET','(BET - ESET) BET - Electronics Technology'),
    ('BET - MT','(BET - MT) BET - Mechanical Technology'),
    ('BET - MET - AT','(BET - MET - AT) BET - MET - Automotive Technology'),
    ('BET - MET - PPT','(BET - MET - PPT) BET - MET - Power Plant Technology'),
    ('BSIE - HE','(BSIE - HE) BSIE - Home Economics'),
    ('BSIE - IA','(BSIE - IA) BSIE - Industrial Arts'),
    ('BSIE - ICT','(BSIE - ICT) BSIE - Information and Communication Technology'),
    ('BTTE - CP','(BTTE - CP) BTTE - Computer Programming'),
    ('BTTE - EL','(BTTE - EL) BTTE - Electrical'),
    ('BGT - AT','(BGT - AT) BGT - Architecture Technology'),]
    firstname1 = models.CharField(max_length=200, null=True,verbose_name="First name")
    middlename= models.CharField(max_length=200, null=True,verbose_name="Middle name")
    lastname = models.CharField(max_length=200, null=True,verbose_name="Last name")
    course = models.CharField(max_length=200, choices=crs)
    daterequest = models.DateTimeField(auto_now_add=True, null=True)
    imagee= models.ImageField( max_length=254)
    conterpersonn= models.CharField(max_length=200, null=True,verbose_name="Contactperson")
    contactnum= models.CharField(max_length=200, null=True,verbose_name="Contactnumber")
    address= models.CharField(max_length=200, null=True,verbose_name="Address")
    studnum= models.CharField(max_length=200, null=True,verbose_name="Student Number")
    signature= models.ImageField(max_length=200, null=True,verbose_name="Signature")
    semail= models.CharField(max_length=200, null=True,verbose_name="Student Email")
    status= models.CharField(max_length=200, null=True, default='P', verbose_name="status")


class Fregistration(models.Model):
    Ffirstname1 = models.CharField(max_length=200, null=True,verbose_name="First name")
    Fmiddlename= models.CharField(max_length=200, null=True,verbose_name="Middle name")
    Flastname = models.CharField(max_length=200, null=True,verbose_name="Last name")
    Femployeenum = models.CharField(max_length=200, null=True,verbose_name="Employee Number")
    Fdaterequest = models.DateTimeField(auto_now_add=True, null=True)
    Fimagee= models.ImageField( max_length=254)
    Fgsis= models.CharField(max_length=200, null=True,verbose_name="GSIS")
    Fgsisno= models.CharField(max_length=200, null=True,verbose_name="GSIS NO")
    Ftin= models.CharField(max_length=200, null=True,verbose_name="TIN")
    Fpagibig= models.CharField(max_length=200, null=True,verbose_name="PAG-IBIG")
    Fphilhealth= models.CharField(max_length=200, null=True,verbose_name="Philhealth")
    Fothers= models.CharField(max_length=200, null=True,verbose_name="Others")
    Fconterpersonn= models.CharField(max_length=200, null=True,verbose_name="Contactperson")
    Fcontactnum= models.CharField(max_length=200, null=True,verbose_name="Contactnumber")
    Faddress= models.CharField(max_length=200, null=True,verbose_name="Address")
    Fsignature= models.ImageField(max_length=200, null=True,verbose_name="Signature")
    femail= models.CharField(max_length=200, null=True,verbose_name="Faculty Email")
    fstatus= models.CharField(max_length=200, null=True, default='P', verbose_name="fstatus")




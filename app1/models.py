from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.PositiveBigIntegerField()
    department=models.ForeignKey(Department,on_delete=models.PROTECT)
    special=models.CharField(max_length=50)
   
    def __str__(self):
        return self.name

    
   
    
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name=models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department=models.ForeignKey(Department,on_delete=models.PROTECT)
    mobile=models.PositiveBigIntegerField()
    address=models.CharField(max_length=50)
    image=models.ImageField(upload_to = 'media/reportimages')
    mailid =models.CharField(max_length=50)
   

    def __str__(self):
        return self.name

class Appointment(models.Model):
    
    doctor=models.ForeignKey(Doctor,on_delete=models.PROTECT)
    patient=models.ForeignKey(Patient,on_delete=models.PROTECT)
    date1=models.DateField()
    time1=models.TimeField()

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name



class Nurses(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name=models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.ForeignKey(Department,on_delete=models.PROTECT)
    mobile=models.PositiveBigIntegerField()
   

    def __str__(self):
        return self.name
    
class SentMail(models.Model):
    to_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.to_email}"

class Document(models.Model):
    
    patient=models.ForeignKey(Patient,on_delete=models.PROTECT)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to = 'media/reportimages')

    def __str__(self):
        return self.patient.name    

class Bed(models.Model):
    
    patient=models.ForeignKey(Patient,on_delete=models.PROTECT)
    nurse=models.ForeignKey(Nurses,on_delete=models.PROTECT)
    department=models.ForeignKey(Department,on_delete=models.PROTECT)
    number=models.PositiveBigIntegerField()
    description=models.CharField(max_length=150)
    date1=models.DateField()
    date2=models.DateField() 

    def __str__(self):
        return self.patient.name
    
class Bill(models.Model):
    STATUS_CHOICE=[('PAID', 'PAID'),
        ('PENDING', 'PENDING'),]
    patient=models.ForeignKey(Patient,on_delete=models.PROTECT)
    number=models.PositiveBigIntegerField()
    
    note=models.CharField(max_length=150)
    date1 = models.DateField()
    status = models.CharField(choices= STATUS_CHOICE,max_length=20)

    def __str__(self):
        return self.patient.name

class GBill(models.Model):
    STATUS_CHOICE=[('PAID', 'PAID'),
        ('PENDING', 'PENDING'),]
    patient=models.ForeignKey(Patient,on_delete=models.PROTECT)
    mailid =models.CharField(max_length=50)
    operation=models.PositiveBigIntegerField()
    medicine=models.PositiveBigIntegerField()
    additional=models.PositiveBigIntegerField()
    tax=models.PositiveBigIntegerField()
    note=models.CharField(max_length=150)
    date1 = models.DateField()
    status = models.CharField(choices= STATUS_CHOICE,max_length=20)

    def __str__(self):
        return self.patient.name
class Invoicemail(models.Model):
    
    mailid =  models.ForeignKey(Patient,on_delete=models.PROTECT)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.to_email}"
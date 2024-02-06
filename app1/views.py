
from django.core.mail import EmailMessage
import os
from urllib import request
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from curesync.settings import EMAIL_HOST_USER
from .forms import *
from app1.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count
from datetime import date, timedelta
from django.utils import timezone
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
import base64
import numpy as np
import pandas as pd
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
# Create your views here.
def Homepage(request):
    
    #if not request.user.is_staff:
    #    return redirect('login')
    doctors=Doctor.objects.all()
    patient=Patient.objects.all()
    appointment=Appointment.objects.all()

    d=0;
    p=0;
    a=0;

    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    d1 = {'d':d,'p':p,'a':a}
    if request.method == "POST":
        
        msg = request.POST.get('message')
        mail = request.POST.get('mailid')
        print(msg,mail)
        #send_mail('sub','msg','hpgadhiya9630@gmail.com',['harshil96300@gmail.com'])
        send_mail("Asking for inquiry as descibed below",msg,'curesync.org@gmail.com',[mail])
        return HttpResponse('email sent successfully')
    
    return render(request,'index.html',d1)

 



def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Pass is wrong")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
        
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            #login(user)
            return redirect('adminmain')
        else:
            return HttpResponse("wrong details")
        print(username)
        

    return render(request,'login.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def format(request):
    return render(request,'format.html')

def departmentmain(request):
    return render(request,'departmentmain.html')
def adminmain12(request):
    return render(request,'adminmain12.html')


######
#Doctor Part start
#####
def viewdoctors(request):
    #if not request.user.is_staff:
    #     return redirect('login')
    doc=Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'viewdoctors.html',d)
        
def adddoctors(request):
    error=""
    #if not request.user.is_staff:
     #   return redirect ('login')
    department1=Department.objects.all()
    if request.method=='POST':
      n = request.POST['name']
   
      c = request.POST['contact']
      de = request.POST['department']
      sp = request.POST['special']
      print(de)
      department = Department.objects.filter(name=de).first()
      try:
          Doctor.objects.create(name=n,mobile=c,department=department,special=sp)
          error="no"
      except:
          error="yes"
    d = {'error':error,'department':department1}
    return render(request,'adddoctors.html',d)

def deletedoctor(request,pid):
   # if not request.user.is_staff:
    #    return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('viewdoctors')
def editdoctor(request,id):
    doctor = Doctor.objects.get(id=id)
    department =Department.objects.all()
    return render(request,'updatedoctor.html',{'doctor':doctor,'department':department,'id':id})
def updatedoctor(request,id):
    print(request)
    update = Doctor.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      n = request.POST.get('name')
      c = request.POST.get('contact')
      d = request.POST.get('department')
      sp = request.POST.get('special')
      update.name=n
      update.mobile=c
      update.department=Department.objects.filter(name=d).first()
      update.special=sp
      update.department.save()
      update.save()
    return redirect('viewdoctors')
######
#Doctor Part start
#####

######
#Patient Part start
#####

def viewpatient(request):
    #if not request.user.is_staff:
    #     return redirect('login')
    pat=Patient.objects.all()
    p = {'pat':pat}
    return render(request,'viewpatient.html',p)
        
def addpatient(request):
    error=""
    #]if not request.user.is_staff:
     #   return redirect ('login')
    department1=Department.objects.all()
    if request.method=='POST':
      na = request.POST['name']
      ge = request.POST['gender']
      mail = request.POST['mailid']
      de = request.POST['department']
      co = request.POST['contact']
      ad = request.POST['address']
      i=request.FILES['image']
      department = Department.objects.filter(name=de).first()
      try:
          Patient.objects.create(name=na,gender=ge,department=department,mailid=mail,mobile=co,address=ad,image=i)
          error="no"
      except:
          error="yes"
    p = {'error':error,'department':department1}
    return render(request,'addpatient.html',p)

def deletepatient(request,aid):
    #if not request.user.is_staff:
    #    return redirect('login')
    patient = Patient.objects.get(id=aid)
    patient.delete()
    return redirect('viewpatient')

def editpatient(request,id):
    department =Department.objects.all()
    patient = Patient.objects.get(id=id)
    return render(request,'updatepatient.html',{'patient':patient,'id':id,'department':department})
def updatepatient(request,id):
    print(request)

    update = Patient.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
              
      n = request.POST.get('name')
      g = request.POST.get('gender')
      mail = request.POST.get('mailid')
      d = request.POST.get('department')
      c = request.POST.get('contact')
      sp = request.POST.get('address')
      update.name=n
      update.gender=g
      update.mailid=mail
      update.department=Department.objects.filter(name=d).first()
      update.mobile=c
      update.address=sp
      update.department.save()
      update.save()
    return redirect('viewpatient')
######
#Patient Part end
#####


######
#Appointment Part Start
#####
def addappointment(request):
    error=""
    #if not request.user.is_staff:
     #   return redirect ('login')
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method=='POST':
      
      d = request.POST['doctor']
      p = request.POST['patient']
      da = request.POST['date']
      ti = request.POST['time']
      doctor = Doctor.objects.filter(name=d).first()
      patient = Patient.objects.filter(name=p).first()
      #doctor = Doctor.objects.all()
      #patient = Patient.objects.all()
      try:
          Appointment.objects.create(doctor=doctor,patient=patient,date1=da,time1=ti)
          error="no"
      except:
          error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'addappointment.html',d)


def viewappointment(request):
    #if not request.user.is_staff:
     #    return redirect('login')
    appoint=Appointment.objects.all()
    p = {'appoint':appoint}
    return render(request,'viewappointment.html',p)

def deleteappointment(request,aid):
    #if not request.user.is_staff:
   #     return redirect('login')
    appointment = Appointment.objects.get(id=aid)
    appointment.delete()
    return redirect('viewappointment')
def editappoint(request,id):
    patient = Patient.objects.all()
    doctor = Doctor.objects.all()
    appoint = Appointment.objects.get(id=id)
    return render(request,'updateappoint.html',{'appoint':appoint,'id':id,'doctor':doctor,'patient':patient})
def updateappoint(request,id):
    print(request)
    update = Appointment.objects.get(id=id)
  
    
    if request.method=='POST':
      na = request.POST.get('patient')
      da = request.POST.get('doctor')
      p = request.POST.get('date')
      sp1 = request.POST.get('time')
      update.patient=Patient.objects.filter(name=na).first()
      update.doctor=Doctor.objects.filter(name=da).first()
      update.date1=p
      update.time1=sp1
      update.patient.save()
      update.doctor.save()
      update.save()
      
    return redirect('viewappointment')

######
#Appointment Part end
#####
def adminmain(request):
    #if not request.user.is_staff:
   #     return redirect('login')
    doctors=Doctor.objects.all()
    patient=Patient.objects.all()
    appointment=Appointment.objects.all()
    nurse=Nurses.objects.all()

    d=0;
    p=0;
    a=0;
    n=0;

    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    for i in nurse:
        n+=1
    d1 = {'d':d,'p':p,'a':a,'n':n}
    return render(request,'adminmain.html',d1)

######
#nurse Part start
#####

def viewnurse(request):
    #if not request.user.is_staff:
     #    return redirect('login')
    nur=Nurses.objects.all()
    p = {'nur':nur}
    return render(request,'viewnurse.html',p)
        
def addnurse(request):
    error=""
   # if not request.user.is_staff:
#return redirect ('login')
    department1=Department.objects.all()
    if request.method=='POST':
      na = request.POST['name']
      ge = request.POST['gender']
      de = request.POST['department']
      co = request.POST['contact']
      department = Department.objects.filter(name=de).first()
      try:
          Nurses.objects.create(name=na,gender=ge,department=department,mobile=co)
          error="no"
      except:
          error="yes"
    p = {'error':error,'department':department1}
    return render(request,'addnurse.html',p)

def deletenurse(request,aid):
   # if not request.user.is_staff:
   #     return redirect('login')
    nurse = Nurses.objects.get(id=aid)
    nurse.delete()
    return redirect('viewnurse')

def editnurse(request,id):
    nurse = Nurses.objects.get(id=id)
    department =Department.objects.all()
    return render(request,'updatenurse.html',{'nurse':nurse,'id':id,'department':department})
def updatenurse(request,id):
    print(request)
    update = Nurses.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      n = request.POST.get('name')
      c = request.POST.get('contact')
      d = request.POST.get('department')
      g = request.POST.get('gender')
      update.name=n
      update.gender=g
      update.department=Department.objects.filter(name=d).first()
      update.mobile=c
      
      update.department.save()
      update.save()
    return redirect('viewnurse')
######
#Nurse Part end
#####

def noticeboard(request):
    return render(request,'noticeboard.html')
def smslist(request):
    return render(request,'smslist.html')
def newsms(request):
    return render(request,'newsms.html')

def messageinbox(request):
    return render(request,'messageinbox.html')
def messagesent(request):
    return render(request,'messagesent.html')
def newmessage(request):
    return render(request,'newmessage.html')





def doctorlist(request):
   # if not request.user.is_staff: 
   #      return redirect('login')
    doc=Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'doctorlist.html',d)

def appointmentlist(request):
   # if not request.user.is_staff:
   #      return redirect('login')
    appoint=Appointment.objects.all()
    p = {'appoint':appoint}
    return render(request,'appointmentlist.html',p)

def patientlist(request):
   # if not request.user.is_staff:
   #      return redirect('login')
    pat=Patient.objects.all()
    p = {'pat':pat}
    return render(request,'patientlist.html',p)
def nurselist(request):
    #if not request.user.is_staff:
    #     return redirect('login')
    nur=Nurses.objects.all()
    p = {'nur':nur}
    return render(request,'nurselist.html',p)

######doctor#########
def documentlist(request):
    #if not request.user.is_staff:
    #     return redirect('login')
    document=Document.objects.all()
    p = {'document':document}
    return render(request,'documentlist.html',p)

def deletedocument(request,aid):
    #if not request.user.is_staff:
    #    return redirect('login')
    document = Document.objects.get(id=aid)
    document.delete()
    return redirect('viewdoc')

######doctor#########
def adddoc(request):
    error=""
    #if not request.user.is_staff:
    #    return redirect ('login')
    
    patient1=Patient.objects.all()
    if request.method=='POST':
      p = request.POST['patient']
      n = request.POST['name']
      i=request.FILES['image']
          
      
      patient = Patient.objects.filter(name=p).first()
      #doctor = Doctor.objects.all()
      #patient = Patient.objects.all()
      try:
          Document.objects.create(patient=patient,name=n,image=i)
          error="no"
      except:
          error="yes"
    d = {'patient':patient1,'error':error}
    return render(request,'adddoc.html',d)


def viewdoc(request):
   # if not request.user.is_staff:
   #      return redirect('login')
    document=Document.objects.all()
    p = {'document':document}
    return render(request,'viewdoc.html',p)

def bedassign(request):
    error=""
   # if not request.user.is_staff:
   #     return redirect ('login')
   
    patient1=Patient.objects.all()
    nurse1=Nurses.objects.all()
    department1=Department.objects.all()
    if request.method=='POST':
      p = request.POST['patient']
      n = request.POST['nurse']
      n1 = request.POST['department']
      nu = request.POST['number']
      de = request.POST['description']
      d1 = request.POST['date1']
      d2 = request.POST['date2']
   
      patient = Patient.objects.filter(name=p).first()
      nurse = Nurses.objects.filter(name=n).first()
      department = Department.objects.filter(name=n1).first()
      
      #doctor = Doctor.objects.all()
      #patient = Patient.objects.all()
      try:
          Bed.objects.create(patient=patient,nurse=nurse,department=department,number=nu,description=de,date1=d1,date2=d2)
          error="no"
          print(department)
      except:
          error="yes"
    p = {'patient':patient1,'nurse':nurse1,'department':department1,'error':error}
    return render(request,'bedassign.html',p)


def bedassignlist(request):
    #if not request.user.is_staff:
     #    return redirect('login')
    bed=Bed.objects.all()
    bed = {'bed':bed}
    return render(request,'bedassignlist.html',bed)

def deletebedassign(request,aid):
    #if not request.user.is_staff:
    #    return redirect('login')
    bed = Bed.objects.get(id=aid)
    bed.delete()
    return redirect('bedassignlist')

def editbedlist(request,id):
    patient = Patient.objects.all()
    nurse = Nurses.objects.all()
    department = Department.objects.all()
    bed = Bed.objects.get(id=id)

    return render(request,'updatebed.html',{'id':id,'bed':bed,'nurse':nurse,'department':department,'patient':patient})
def updatebed(request,id):
    print(request)
    #bill1 = Patient.objects.filter(name=p).first()
    update = Bed.objects.get(id=id)
  
    if request.method=='POST':
      n1  = request.POST.get('patient')
      na  = request.POST.get('nurse')
      d  = request.POST.get('department')
      n  = request.POST.get('number')
      no = request.POST.get('description')
      da = request.POST.get('date1')
      da1 = request.POST.get('date2')
      update.patient=Patient.objects.filter(name=n1).first()
      update.nurse=Nurses.objects.filter(name=na).first()
      update.department=Department.objects.filter(name=d).first()
      update.number=n
      update.description=no
      update.date1=da
      update.date2=da1
      update.patient.save()
      update.nurse.save()
      update.department.save()
      
      update.save()
    
    return redirect('bedassignlist')



def graph(request):
    start_date ="2024-01-08"
    end_date  = "2024-01-24"
    date_object = date.fromisoformat(start_date)
    date_object1 = date.fromisoformat(end_date)



    # Query the database to get the count of appointments for each date in the range
    appointments_count = Appointment.objects.filter(date1__range=[date_object, date_object1])\
                                           .values('date1')\
                                           .annotate(count=Count('id'))

    # Extract data for plotting
    dates = [entry['date1'] for entry in appointments_count]
    counts = [entry['count'] for entry in appointments_count]
  

    # Your data (replace this with your actual data)
    #x = [dates]
    #y = [counts]
   
    # Create the line chart
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.plot(dates,counts)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Line Chart Example')
    plt.legend()

    plt.tight_layout()

    # Save the chart to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='jpg')
    buffer.seek(0)
    plt.close()

    # Convert the buffer to base64 encoding
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    context = {'image_base64': image_base64}
    # Pass the base64-encoded image to the template
    #context = {'image_base64': image_base64}
    
    return render(request, 'graph.html',context)


######
#Bill Part Start
#####
def addbill(request):
    error=""
   # if not request.user.is_staff:
   #     return redirect ('login')
    patient1=Patient.objects.all()
    if request.method=='POST':
      
     
      p = request.POST['patient']
      n = request.POST['number']
      no = request.POST['note']
      da = request.POST['date']
      sa = request.POST['status']
      
      patient = Patient.objects.filter(name=p).first()
      
      try:
          Bill.objects.create(patient=patient,number=n,note=no,date1=da,status=sa)
          error="no"
      except:
          error="yes"
    d = {'patient':patient1,'error':error}
    return render(request,'addbill.html',d)


def viewbill(request):
   # if not request.user.is_staff:
   #      return redirect('login')
    bill=Bill.objects.all()
    p = {'bill':bill}
    return render(request,'viewbill.html',p)

def deletebill(request,aid):
    #if not request.user.is_staff:
    #    return redirect('login')
    bill = Bill.objects.get(id=aid)
    bill.delete()
    return redirect('viewbill')
def editbill(request,id):
    patient = Patient.objects.all()
    bill = Bill.objects.get(id=id)

    return render(request,'updatebill.html',{'id':id,'bill':bill,'patient':patient})
def updatebill(request,id):
    
    
    #bill1 = Patient.objects.filter(name=p).first()
    update = Bill.objects.get(id=id)
  
    if request.method=='POST':
      p = request.POST.get('patient')
      n  = request.POST.get('number')
      no = request.POST.get('note')
      da = request.POST.get('date')
      sa = request.POST.get('status')
       
      update.patient=Patient.objects.filter(name=p).first()
    
      update.number=n
      update.note=no
      update.date1=da
      update.status=sa
      update.patient.save()
      update.save()
      
    return redirect('viewbill')

######
#Bill Part end
#####
######
#Department Part start
#####
def viewdepartment(request):
    #if not request.user.is_staff:
     #    return redirect('login')
    department=Department.objects.all()
    d = {'department':department}
    return render(request,'viewdepartment.html',d)
        
def adddepartment(request):
    error=""
    #if not request.user.is_staff:
     #   return redirect ('login')
    if request.method=='POST':
      n = request.POST['name']
     
      try:
          Department.objects.create(name=n)
          error="no"
      except:
          error="yes"
    d = {'error':error}
    return render(request,'adddepartment.html',d)

def deletedepartment(request,qid):
    #if not request.user.is_staff:
    #    return redirect('login')
    department = Department.objects.get(id=qid)
    department.delete()
    return redirect('viewdepartment')

def editdepartment(request,id):
    department = Department.objects.get(id=id)
    return render(request,'updatedepartment.html',{'department':department,'id':id})
def updatedepartment(request,id):
    print(request)
    update = Department.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      n = request.POST.get('name')
      update.name=n
      update.save()
    return redirect('viewdepartment')
######
#Department Part start
#####



def multiple_line_charts(request):
    
   

    patient_count = Patient.objects.values('department')\
                                  .annotate(count1=Count('id'))

    # Extract data for plotting
    departments = [entry['department'] for entry in patient_count]
    counts1 = [entry['count1'] for entry in patient_count]
   
    nurse_count = Nurses.objects.values('department')\
                                  .annotate(count2=Count('id'))

    # Extract data for plotting
    departments = [entry['department'] for entry in nurse_count]
    counts2 = [entry['count2'] for entry in nurse_count]

    # Create the line chart
    plt.switch_backend('AGG')
    plt.plot(departments,counts2)
    plt.plot(departments,counts1)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Line Chart Example')

    # Save the chart to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    
   
    # Convert the buffer to base64 encoding
    image_base65 = base64.b64encode(buffer.read()).decode('utf-8')
    
    # Pass the base64-encoded image to the template
    context = {'image_base65': image_base65}
    return render(request, 'multiple_line_charts.html', context)
    
    
def admindoctor(request):
    
    #if not request.user.is_staff:
     #   return redirect('login')
    doctors=Doctor.objects.all()
    patient=Patient.objects.all()
    appointment=Appointment.objects.all()

    d=0;
    p=0;
    a=0;

    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    #d1 = {'d':d,'p':p,'a':a}
    start_date ="2024-01-08"
    end_date  = "2024-01-31"
    date_object = date.fromisoformat(start_date)
    date_object1 = date.fromisoformat(end_date)



    # Query the database to get the count of appointments for each date in the range
    appointments_count = Appointment.objects.filter(date1__range=[date_object, date_object1])\
                                           .values('date1')\
                                           .annotate(count=Count('id'))

    # Extract data for plotting
    dates = [entry['date1'] for entry in appointments_count]
    counts = [entry['count'] for entry in appointments_count]
  

    # Your data (replace this with your actual data)
    #x = [dates]
    #y = [counts]   
   
    # Create the line chart
   
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.plot(dates,counts,marker='o', linestyle='-',label='Appointment Line ')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Appointment Chart')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Save the chart to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='jpg')
    buffer.seek(0)
    plt.close()
   #
   #
   #
   #
    print(dates)
    date1=['2024, 1, 26','2024, 1, 27','2024, 1, 28','2024, 1, 29','2024, 1, 30']
    departments = Department.objects.values_list('name', flat=True)

    # Convert the list to a single comma-separated string
    
    patient_count = Patient.objects.values('department')\
                                  .annotate(count1=Count('id'))

    # Extract data for plotting
    #departments = [entry['department'] for entry in patient_count]
    counts1 = [entry['count1'] for entry in patient_count]
   
    nurse_count = Nurses.objects.values('department')\
                                  .annotate(count2=Count('id'))

    # Extract data for plotting
    #departments = [entry['department'] for entry in nurse_count]
    counts2 = [entry['count2'] for entry in nurse_count]

    doctors_count = Doctor.objects.values('department')\
                                  .annotate(count3=Count('id'))

    # Extract data for plotting
    #departments = [entry['department'] for entry in doctors_count]
    counts3 = [entry['count3'] for entry in doctors_count]
    # Create the line chart
    plt.switch_backend('AGG')
    plt.plot(departments,counts3,marker='o', linestyle='dotted',label='Doctor Line ')
    plt.plot(departments,counts1,marker='o', linestyle='dashdot',label='Patient Line ')
    plt.plot(departments,counts2,marker='o', linestyle='--',label='Nurse Line ')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Detailed Chart')
    plt.legend()
    plt.tight_layout()

    # Save the chart to a BytesIO buffer
    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    plt.close()

    # Convert the buffer to base64 encoding
    image_base65 = base64.b64encode(buffer1.read()).decode('utf-8')
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    dep1 = ['January', 'February', 'March', 'April', 'May']
    #context = {'image_base64': image_base64}
    z= {'image_base64': image_base64,'d':d,'image_base65':image_base65,'p':p,'a':a,'departments':departments,'counts3': counts3,'counts2':counts2,'counts1':counts1,'dep1':dep1,'nurse_count':nurse_count,'doctors_count':doctors_count,'date1':date1,'counts':counts}
    return render(request,'admindoctor.html',z)


def chartview(request):
    
        dep1 = ['January', 'February', 'March', 'April', 'May']
        value = [10, 20, 15, 25, 30]
        value1 = [11, 7, 30, 12, 24]
        #departments = Department.objects.all()
       # dep1 = [department.name for department in departments]


    # Convert the list to a single comma-separated string
    
        patient_count = Patient.objects.values('department')\
                                  .annotate(count1=Count('id'))

    # Extract data for plotting
    #departments = [entry['department'] for entry in patient_count]
        counts1 = [entry['count1'] for entry in patient_count]
   
        nurse_count = Nurses.objects.values('department')\
                                  .annotate(count2=Count('id'))

    # Extract data for plotting
    #departments = [entry['department'] for entry in nurse_count]
        counts2 = [entry['count2'] for entry in nurse_count]

        doctors_count = Doctor.objects.values('department')\
                                  .annotate(count3=Count('id'))
        appointments = Appointment.objects.order_by('date')
        appointment_dates = [appointment.date for appointment in appointments]
    # Extract data for plotting
    #departments = [entry['department'] for entry in doctors_count]
        counts3 = [entry['count3'] for entry in doctors_count]
        z = {'counts3': counts3,'counts2':counts2,'counts1':counts1,'dep1':dep1,'value':value,'appointment_dates':appointment_dates,'doctors_count':doctors_count,'date1':date1}
        return render(request, 'chartview.html', z)

def invoice(request):
    return render(request,'invoice.html')
def pdf(request):
    if request.method=='POST':
      o = request.POST['operation']
      m = request.POST['medicine']
      a = request.POST['additional']
      t = request.POST['tax']
      dt = request.POST['date']
      
      total= int(o)+int(m)+int(a)+int(t) 
   
      return render(request,'pdf.html',{'o':o,'m':m,'a':a,'t':t,'dt':dt,'total':total})
    return render(request,'invoice.html')


def viewgbill(request):
   # if not request.user.is_staff:
   #      return redirect('login')
    bill=GBill.objects.all()
    p = {'bill':bill}
    return render(request,'viewgbill.html',p)


def deletegbill(request,aid):
    #if not request.user.is_staff:
    #    return redirect('login')
    bill = GBill.objects.get(id=aid)
    bill.delete()
    return redirect('viewgbill')

def updategbill(request,id):
    
    
    #bill1 = Patient.objects.filter(name=p).first()
    update = GBill.objects.get(id=id)
  
    if request.method=='POST':
      p = request.POST.get('patient')
      o = request.POST.get('operation')
      m = request.POST.get('medicine')
      a = request.POST.get('additional')
      t = request.POST.get('tax')
      no = request.POST.get('note')
      da = request.POST.get('date')
      sa = request.POST.get('status')
       
      update.patient=Patient.objects.filter(name=p).first()
    
      update.operation=o
      update.medicine=m
      update.additional=a
      update.tax=t
      update.note=no
      update.date1=da
      update.status=sa
      update.patient.save()
      update.save()
      
    return redirect('viewgbill')

def addgbill(request):
    error=""
   # if not request.user.is_staff:
   #     return redirect ('login')
    patient1=Patient.objects.all()
    if request.method=='POST':
      
     
      p = request.POST['patient']
      ma = request.POST['mailid']
      o = request.POST['operation']
      m = request.POST['medicine']
      a = request.POST['additional']
      t = request.POST['tax']
      no = request.POST['note']
      da = request.POST['date']
      sa = request.POST['status']
      
      patient = Patient.objects.filter(name=p).first()
      
      try:
          GBill.objects.create(patient=patient,operation=o,medicine=m,additional=a,mailid=ma,tax=t,note=no,date1=da,status=sa)
          error="no"
      except:
          error="yes"
    d = {'patient':patient1,'error':error}
    return render(request,'addgbill.html',d)
def editgbill(request,id):
    patient = Patient.objects.all()
    bill = GBill.objects.get(id=id)

    return render(request,'updategbill.html',{'id':id,'bill':bill,'patient':patient})


def invoicelist(request):
   # if not request.user.is_staff:
   #      return redirect('login')
    bill=GBill.objects.all()
    p = {'bill':bill}
    return render(request,'invoicelist.html',p)
def editinvoice(request,id):
    patient = Patient.objects.all()
    bill = GBill.objects.get(id=id)

    return render(request,'getinvoice.html',{'id':id,'bill':bill,'patient':patient})

def getinvoice(request,id):
    
    
    #bill1 = Patient.objects.filter(name=p).first()
    update = GBill.objects.get(id=id)
  
    if request.method=='POST':
      p = request.POST.get('patient')
      mail = request.POST.get('mailid')
      o = request.POST.get('operation')
      m = request.POST.get('medicine')
      a = request.POST.get('additional')
      t = request.POST.get('tax')
      no = request.POST.get('note')
      da = request.POST.get('date')
      
       
      update.patient=Patient.objects.filter(name=p).first()
      update.mailid=mail  
      update.operation=o
      update.medicine=m
      update.additional=a
      update.tax=t
      update.note=no
      update.date1=da
      
      update.patient.save()
      update.save()
      
    return redirect('finalinvoice')

#def finalinvoice(request):
    if request.method=='POST':
      p = request.POST['patient']
      o = request.POST['operation']
      m = request.POST['medicine']
      a = request.POST['additional']
      t = request.POST['tax']
      no = request.POST['note']
      dt = request.POST['date']
      print("okok",o,m,a,t,dt)
      total= int(o)+int(m)+int(a)+int(t) 
      print("Total amount is :",total) 
      return render(request,'finalinvoice.html',{'p':p,'no':no,'o':o,'m':m,'a':a,'t':t,'dt':dt,'total':total})
    return render(request,'viewgbill.html')

def invoicegen(request):
    error=""
   # if not request.user.is_staff:
   #     return redirect ('login')
    patient1=Patient.objects.all()
    if request.method=='POST':
      
     
      p = request.POST['patient']
      o = request.POST['operation']
      m = request.POST['medicine']
      a = request.POST['additional']
      t = request.POST['tax']
      no = request.POST['note']
      da = request.POST['date']
      sa = request.POST['status']
      
      patient = Patient.objects.filter(name=p).first()
      
      try:
          GBill.objects.create(patient=patient,operation=o,medicine=m,additional=a,tax=t,note=no,date1=da,status=sa)
          error="no"
      except:
          error="yes"
    d = {'patient':patient1,'error':error}
    return render(request,'invoicegen.html',d)

def invoicelast(request):
    return render(request,'invoicelast.html')

######
#Bill Part end


def sendmail(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        mail = request.POST.get('mailid')
        print(sub,msg,mail)
        #send_mail('sub','msg','hpgadhiya9630@gmail.com',['harshil96300@gmail.com'])
        send_mail(sub,msg,'curesync.org@gmail.com',[mail])
        return HttpResponse('email sent successfully')
    return render(request,'sendmail.html')
######doctor#########
def admindoctor12(request):
    return render(request,'admindoctor12.html')
def mailat(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        mail = request.POST.get('mailid')
        file = request.FILES.get("file")
        #output=BytesIO()
        #file.save(output)

        file_content = file.read()
        output = BytesIO()
        output.write(file_content)
        output.seek(0)

        email = EmailMessage(
            sub,
            msg,
            settings.EMAIL_HOST_USER ,
            [mail]
            )
       
        
        email.attach(
            file.name,
            output.getvalue(),
            file.content_type
        )
        email.send()
        return HttpResponse('email sent successfully')
    return render(request,'mailat.html')
def invoicemail(request):
    error=""
    #if not request.user.is_staff:
     #   return redirect ('login')
    
    invoicemail=Patient.objects.all()
    
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        mail = request.POST.get('mailid')
        file = request.FILES.get("file")
        #output=BytesIO()
        #file.save(output)

        file_content = file.read()
        output = BytesIO()
        output.write(file_content)
        output.seek(0)

        email = EmailMessage(
            sub,
            msg,
            settings.EMAIL_HOST_USER ,
            [mail]
            )
       
        
        email.attach(
            file.name,
            output.getvalue(),
            file.content_type
        )
       
        try:
            email.send()
          #  error=('no')
            messages.success(request,"Mail sent successfully")
            
            
        except:
         # error="yes"
          messages.error(request,"Failed to send mail")
            
         
        #return HttpResponse('email sent successfully')
    
    d = {'invoicemail':invoicemail,'error':error}
    return render(request,'invoicemail.html',d)


def generate_pdf(html_content, file_path):
    # Generate PDF from HTML content
    with open(file_path, 'w+b') as pdf_file:
        pisa.CreatePDF(html_content, dest=pdf_file)

def finalinvoice(request):
    if request.method=='POST':
      p = request.POST['patient']
      m = request.POST['mailid']
      o = request.POST['operation']
      m = request.POST['medicine']
      a = request.POST['additional']
      t = request.POST['tax']
      no = request.POST['note']
      dt = request.POST['date']
      print("okok",o,m,a,t,dt)
      total= int(o)+int(m)+int(a)+int(t) 
      
      
      return render(request,'finalinvoice.html',{'p':p,'no':no,'o':o,'m':m,'a':a,'t':t,'dt':dt,'total':total})
    return render(request,'viewgbill.html')

def readyinvoice(request):
      html_content =render_to_string('finalinvoice.html', {'context_variable': 'value'})
      pdf_file_path = 'temporary_file.pdf'
      generate_pdf(html_content, pdf_file_path)
      subject = 'Subject of your email'
      from_email = 'curesync.org@gmail.com'
      to_email = 'hpgadhiya9630@gmail.com'
     
      with open(pdf_file_path, 'rb') as pdf_file:
        email = EmailMessage(subject, 'Text content of your email', from_email, [to_email])
        email.attach('invoice.pdf', pdf_file.read(), 'application/pdf')
        email.send()
        return HttpResponse('email sent successfully') #  error=('no')
   


def readyinvoice1(request):

      p = request.POST.get('patient')
      o = request.POST.get('operation')
      m = request.POST.get('medicine')
      a = request.POST.get('additional')
      t = request.POST.get('tax')
      no = request.POST.get('note')
      dt = request.POST.get('date')
      total = request.POST.get('total')
      print(o)
      print(a)
      print(t)
      print(no)
      
      
      print(total)
      html_content =render_to_string('finalinvoice.html', {'patient':p,'no':no,'o':o,'m':m,'a':a,'t':t,'dt':dt,'total':total})
      pdf_file_path = 'temporary_file.pdf'
      generate_pdf(html_content, pdf_file_path)
      subject = 'Subject of your email'
      from_email = 'curesync.org@gmail.com'
      to_email = 'hpgadhiya9630@gmail.com'
     
      with open(pdf_file_path, 'rb') as pdf_file:
        email = EmailMessage(subject, 'Text content of your email', from_email, [to_email])
        email.attach('invoice.pdf', pdf_file.read(), 'application/pdf')
        email.send()
        return HttpResponse('email sent successfully')
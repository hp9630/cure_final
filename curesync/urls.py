from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage,name='index'),

    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('format/',views.format,name='format'),
    path('contact/',views.contact,name='contact'),
    path('departmentmain/',views.departmentmain,name='departmentmain'),
    path('service/',views.service,name='service'),
    path('about/',views.about,name='about'),
    path('adminmain/',views.adminmain,name='adminmain'),
    path('viewdoctors/',views.viewdoctors,name='viewdoctors'),
    path('adddoctors/',views.adddoctors,name='adddoctors'),
    path('deletedoctor(?P<int:pid>)',views.deletedoctor,name='deletedoctor'),
    path('editdoctor(<int:id>)',views.editdoctor,name='editdoctor'),
    path('updatedoctor(<int:id>)',views.updatedoctor,name='updatedoctor'),
    path('addpatient/',views.addpatient,name='addpatient'),
    path('viewpatient/',views.viewpatient,name='viewpatient'),

    path('deletepatient(?P<int:aid>)',views.deletepatient,name='deletepatient'),
    path('editpatient(<int:id>)',views.editpatient,name='editpatient'),
    path('updatepatient(<int:id>)',views.updatepatient,name='updatepatient'),




    path('addappointment/',views.addappointment,name='addappointment'),
    path('viewappointment/',views.viewappointment,name='viewappointment'),
    path('deleteappointment(?P<int:aid>)',views.deleteappointment,name='deleteappointment'),
    path('editappoint(<int:id>)',views.editappoint,name='editappoint'),
    path('updateappoint(<int:id>)',views.updateappoint,name='updateappoint'),

    path('adminmain12/',views.adminmain12,name='adminmain12'),
    path('admindoctor/',views.admindoctor,name='admindoctor'),
    
    

    path('addnurse/',views.addnurse,name='addnurse'),
    path('viewnurse/',views.viewnurse,name='viewnurse'),
    path('deletenurse(?P<int:aid>)',views.deletenurse,name='deletenurse'),
    path('editnurse(<int:id>)',views.editnurse,name='editnurse'),
    path('updatenurse(<int:id>)',views.updatenurse,name='updatenurse'),

    path('addbill/',views.addbill,name='addbill'),
    path('viewbill/',views.viewbill,name='viewbill'),
    path('deletebill(?P<int:aid>)',views.deletebill,name='deletebill'),
    path('editbill(<int:id>)',views.editbill,name='editbill'),
    path('updatebill(<int:id>)',views.updatebill,name='updatebill'),


    path('multiple_line_charts/',views.multiple_line_charts,name='multiple_line_charts'),
    path('noticeboard/',views.noticeboard,name='noticeboard'),
    path('sendmail/',views.sendmail,name='sendmail'),
    path('newmessage/',views.newmessage,name='newmessage'),
    path('messagesent/',views.messagesent,name='messagesent'),
    path('messageinbox/',views.messageinbox,name='messageinbox'),
    path('smslist/',views.smslist,name='smslist'),
    path('newsms/',views.newsms,name='newsms'),

    
   # path('simple_chatbot/',SimpleChatbot.as_view())
    

    #admindoctor
    path('admindoctor12/',views.admindoctor12,name='admindoctor12'),
    
    path('doctorlist/',views.doctorlist,name='doctorlist'),
    
    path('patientlist/',views.patientlist,name='patientlist'),
    path('appointmentlist/',views.appointmentlist,name='appointmentlist'),
    path('nurselist/',views.nurselist,name='nurselist'),
    
    path('adddoc/',views.adddoc,name='adddoc'),
    path('viewdoc/',views.viewdoc,name='viewdoc'),
    path('deletedocument(?P<int:aid>)',views.deletedocument,name='deletedocument'),
    path('documentlist/',views.documentlist,name='documentlist'),
     path('bedassign/',views.bedassign,name='bedassign'),
    path('bedassignlist/',views.bedassignlist,name='bedassignlist'),
    path('deletebedassign(?P<int:aid>)',views.deletebedassign,name='deletebedassign'),

    path('editbedlist(<int:id>)',views.editbedlist,name='editbedlist'),
    path('updatebed(<int:id>)',views.updatebed,name='updatebed'),
    
    
    path('viewdepartment/',views.viewdepartment,name='viewdepartment'),
    path('adddepartment/',views.adddepartment,name='adddepartment'),
    path('deletedepartment(?P<int:qid>)',views.deletedepartment,name='deletedepartment'),
    path('editdepartment(<int:id>)',views.editdepartment,name='editdepartment'),
    path('updatedepartment(<int:id>)',views.updatedepartment,name='updatedepartment'),
    
    
    path('graph/',views.graph,name='graph'),
    path('chartview/',views.chartview,name='chartview'),
    #
    #EXPORT DATA
    #
    path('invoice/',views.invoice,name='invoice'),
    path('pdf/',views.pdf,name='pdf'),

    path('addgbill/',views.addgbill,name='addgbill'),
    path('viewgbill/',views.viewgbill,name='viewgbill'),
    path('deletegbill(?P<int:aid>)',views.deletegbill,name='deletegbill'),
    path('editgbill(<int:id>)',views.editgbill,name='editgbill'),
    path('updategbill(<int:id>)',views.updategbill,name='updategbill'),
    path('finalinvoice/',views.finalinvoice,name='finalinvoice'),
    path('invoicegen/',views.invoicegen,name='invoicegen'),
    path('invoicelist/',views.invoicelist,name='invoicelist'),
    path('getinvoice(<int:id>)',views.getinvoice,name='getinvoice'),
    path('editinvoice(<int:id>)',views.editinvoice,name='editinvoice'),

    path('mailat/',views.mailat,name='mailat'),
    path('invoicemail/',views.invoicemail,name='invoicemail'),
    path('readyinvoice/',views.readyinvoice,name='readyinvoice'),
    path('invoicelast/',views.invoicelast,name='invoicelast'),
    path('readyinvoice1/',views.readyinvoice1,name='readyinvoice1'),
   
 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


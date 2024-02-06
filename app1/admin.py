from django.contrib import admin

from app1.models import *

from import_export.admin import ImportExportModelAdmin

class DepartmentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','name']

class DoctorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','name','mobile','department','special']

class PatientAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','name','gender','department','mobile','address','image']

class AppointmentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','doctor','patient','date1','time1']

class NursesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','name','gender','department','mobile']

class SendmailAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','to_email','subject','body','sent_at']
class BedAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','patient','nurse','department','number','description','date1','date2']

class BillAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','patient','number','note','date1','status']
class GBillAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','patient','operation','medicine','additional','tax','note','date1','status']

class DocumentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','patient','name','image']
# Register your models here.
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Nurses,NursesAdmin)
admin.site.register(SentMail,SendmailAdmin)
admin.site.register(Bed,BedAdmin)
admin.site.register(Bill,BillAdmin)
admin.site.register(Document,DocumentAdmin)
admin.site.register(GBill,GBillAdmin)



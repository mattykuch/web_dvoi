from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'district', 'month', 'submitter', 'title_submitter']


    

admin.site.register(District)
admin.site.register(Vaccine)
admin.site.register(Order)
admin.site.register(OrderLine)

from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'district', 'month', 'submitter', 'title_submitter']

    
admin.site.register(Order)

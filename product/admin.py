from django.contrib import admin
from . models import *
# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class proadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','price','stock','desc']
    list_editable=['price','stock','desc']


admin.site.register(categ,catadmin)
admin.site.register(product,proadmin)
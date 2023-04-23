from django.contrib import admin
from .models import Course_product

# Register your models here.

class Course_productAdmin(admin.ModelAdmin):
    list_display =('category', 'course_name', 'image', 'date_created')
    prepopulated_fields = {'slug': ('course_name',)}

admin.site.register(Course_product)




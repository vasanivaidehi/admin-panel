from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','phone','joined_date')
    search_fields = ("firstname__startswith", )


  
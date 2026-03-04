from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','phone','joined_date')
    search_fields = ("firstname__startswith", )


  
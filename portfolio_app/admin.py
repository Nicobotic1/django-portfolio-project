from django.contrib import admin
from .models import Student, Portfolio, Project

# Register your models here. Need to register them to see them in the admin field.

admin.site.register(Student)
admin.site.register(Portfolio)

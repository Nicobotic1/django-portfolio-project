from django.contrib import admin
from .models import Student
from .models import Portfolio

# Register your models here. Need to register them to see them in the admin field.

admin.site.register(Student)
admin.site.register(Portfolio)

from django.contrib import admin

# Register your models here.
from Employee.models import *

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(TaskTracking)

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, null=True)
    create_date=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    empid = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    doj = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    create_date=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.user.first_name
class Task(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    priority = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    work = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=100, null=True)
    assignDate=models.DateTimeField(auto_now=True,null=True)
    endDate=models.DateTimeField(null=True)
    def __str__(self):
        return self.title


class TaskTracking(models.Model):
    taskId = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    remark = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    workCompleted = models.CharField(max_length=100, null=True)
    updationDate = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.taskId.title+" "+self.taskId










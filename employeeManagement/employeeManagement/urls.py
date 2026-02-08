"""employeeManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Employee.views import *
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('login_admin/', Login_admin, name='login_admin'),
    path('login_emp/', Login_Employee, name='login_emp'),
    path('emp_Change_Password/', Emp_Change_Password, name='emp_Change_Password'),
    path('admin_Change_Password/', Admin_Change_Password, name='admin_Change_Password'),
    path('logout/', Logout, name='logout'),
    path('admin_home/', admin_home, name='admin_home'),
    path('emp_home/', emp_home, name='emp_home'),
    path('add_department/', add_department, name='add_department'),
    path('view_department/', view_department, name='view_department'),
    path('update_department/<int:pid>', update_department, name='update_department'),
    path('delete_department/<int:pid>', delete_department, name='delete_department'),
    path('add_employee/', add_employee, name='add_employee'),
    path('edit_employee/<int:pid>', edit_employee, name='edit_employee'),
    path('delete_employee/<int:pid>', delete_employee, name='delete_employee'),
    path('view_employee/', view_employee, name='view_employee'),
    path('checkid/', checkid, name='checkid'),
    path('add_task/', add_task, name='add_task'),
    path('dropdown/', dropdown, name='dropdown'),
    path('emp_new_task/', emp_new_task, name='emp_new_task'),
    path('emp_inprogress_task/', emp_inprogress_task, name='emp_inprogress_task'),
    path('emp_completed_task/', emp_completed_task, name='emp_completed_task'),
    path('emp_all_task/', emp_all_task, name='emp_all_task'),
    path('emp_edit_employee/', emp_edit_employee, name='emp_edit_employee'),
    path('new_task_detail/<int:pid>', new_task_detail, name='new_task_detail'),
    path('update_task_tracker/<int:pid>', updateTaskTracker, name='update_task_tracker'),
    path('admin_view_new_task/', admin_view_new_task, name='admin_view_new_task'),
    path('admin_view_inprogress_task/', admin_view_inprogress_task, name='admin_view_inprogress_task'),
    path('admin_view_completed_task/', admin_view_completed_task, name='admin_view_completed_task'),
    path('admin_view_task_detail/<int:pid>', admin_view_task_detail, name='admin_view_task_detail'),
    path('find_by_date/', find_by_date, name='find_by_date'),
    path('search_employee/', search_employee, name='search_employee'),
    path('view_emp_task/<int:pid>', view_emp_task, name='view_emp_task'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

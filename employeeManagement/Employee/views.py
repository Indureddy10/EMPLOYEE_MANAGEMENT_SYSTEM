from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
# Create your views here.

def Home(request):
    return render(request,'index.html')
def Login_admin(request):
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        print(u)
        user = authenticate(username=u, password=p)
        sign = ""
        try:
            if user.is_staff:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('admin_home')
        except:
            messages.success(request, "Invalid user")
    return render(request, 'admin_login.html')
@login_required(login_url='/login_admin/')
def admin_home(request):
    Emp = Employee.objects.all()
    Dept = Department.objects.all()
    task = Task.objects.all()
    newtask = Task.objects.filter(status="Not Updated Yet")
    inprogresstask = Task.objects.filter(status="Inprogress")
    completedtask = Task.objects.filter(status="Completed")
    Emp=Emp.count()
    Dept=Dept.count()
    task = task.count()
    newtask = newtask.count()
    inprogresstask = inprogresstask.count()
    completedtask = completedtask.count()
    return render(request,'admin_home.html',locals())
@login_required(login_url='/login_emp/')
def emp_home(request):
    emp = Employee.objects.get(user=request.user)
    task = Task.objects.filter(emp=emp)
    newtask = Task.objects.filter(emp=emp,status="Not Updated Yet")
    inprogresstask = Task.objects.filter(emp=emp,status="Inprogress")
    completedtask = Task.objects.filter(emp=emp,status="Completed")
    task=task.count()
    newtask=newtask.count()
    inprogresstask=inprogresstask.count()
    completedtask=completedtask.count()
    return render(request,'emp_home.html',locals())
@login_required(login_url='/login_admin/')
def add_department(request):
    if request.method == 'POST':
        d = request.POST['department']
        Department.objects.create(name=d)
        messages.success(request, "Registration Successful")
        return redirect('view_department')
    return render(request,'add_department.html')
@login_required(login_url='/login_admin/')
def update_department(request,pid):
    data=Department.objects.get(id=pid)
    if request.method == 'POST':
        d = request.POST['department']
        data.name=d
        data.save()
        messages.success(request, "Updation Successful")
        return redirect('view_department')
    return render(request,'update_department.html',{'data':data})
@login_required(login_url='/login_admin/')
def delete_department(request,pid):
    data=Department.objects.get(id=pid)
    data.delete()
    messages.success(request, "delete Successful")
    return redirect('view_department')
@login_required(login_url='/login_admin/')
def view_department(request):
    data=Department.objects.all()
    return render(request,'view_department.html',{'data':data})
@login_required(login_url='/login_admin/')
def add_employee(request):
    deptdata=Department.objects.all()
    emp=Employee.objects.all()
    empid = Employee.objects.filter().last()
    if empid:
        empmainid=int(empid.empid)+1
    else:
        empmainid=1000

    if request.method == 'POST':
        d = request.POST['departmentid']
        eid = request.POST['eid']
        en = request.POST['name']
        e = request.POST['email']
        c = request.POST['contact']
        ed = request.POST['designation']
        dob = request.POST['dob']
        add = request.POST['address']
        doj = request.POST['doj']
        des= request.POST['description']
        pas= request.POST['password']
        img= request.FILES['img']
        dept=Department.objects.get(id=d)
        user=User.objects.create_user(username=eid,email=e,password=pas,first_name=en)
        Employee.objects.create(user=user,dept=dept,empid=eid,contact=c,designation=ed,dob=dob,doj=doj,description=des,address=add,image=img)
        messages.success(request, "Registration Successful")
        return redirect('view_employee')
    return render(request,'add_employee.html',locals())
@login_required(login_url='/login_admin/')
def edit_employee(request,pid):
    deptdata=Department.objects.all()
    emp=Employee.objects.get(id=pid)
    if request.method == 'POST':
        d = request.POST['departmentid']
        eid = request.POST['eid']
        en = request.POST['name']
        e = request.POST['email']
        c = request.POST['contact']
        ed = request.POST['designation']
        dob = request.POST['dob']
        add = request.POST['address']
        doj = request.POST['doj']
        des= request.POST['description']
        dept=Department.objects.get(id=d)
        emp.dept=dept
        emp.empid=eid
        emp.user.first_name=en
        emp.user.email=e
        emp.contact=c
        emp.designation=ed
        emp.dob=dob
        emp.doj=doj
        emp.address=add
        emp.description=des
        try:
            im = request.FILES['img']
            emp.image = im
            emp.save()
        except:
            pass
        emp.user.save()
        emp.save()
        messages.success(request, "Updetation Successful")
        return redirect('view_employee')
    return render(request,'edit_employee.html',locals())
@login_required(login_url='/login_emp/')
def emp_edit_employee(request):
    deptdata=Department.objects.all()
    emp=Employee.objects.get(user=request.user)
    if request.method == 'POST':
        en = request.POST['name']
        e = request.POST['email']
        c = request.POST['contact']
        ed = request.POST['designation']
        dob = request.POST['dob']
        add = request.POST['address']
        doj = request.POST['doj']
        des= request.POST['description']
        emp.user.first_name=en
        emp.user.email=e
        emp.contact=c
        emp.designation=ed
        emp.dob=dob
        emp.doj=doj
        emp.address=add
        emp.description=des
        try:
            im = request.FILES['img']
            emp.image = im
            emp.save()
        except:
            pass
        emp.user.save()
        emp.save()
        messages.success(request, "Updetation Successful")
        return redirect('emp_home')
    return render(request,'emp_edit_employee.html',locals())

def checkid(request):
    try:
        data=Employee.objects.get(user__email=request.GET['mainid'])
        dict = {'status':False, 'message':"Email is already Exist"}
    except:
        dict = {'status':True ,'message': "Unique Email"}
    return JsonResponse(dict)
@login_required(login_url='/login_admin/')
def view_employee(request):
    data=Employee.objects.all()
    return render(request,'view_employee.html',{'data':data})
@login_required(login_url='/login_admin/')
def delete_employee(request,pid):
    pat = User.objects.get(id=pid)
    pat.delete()
    messages.success(request,'Employee Deleted Successfully')
    return redirect('view_employee')
@login_required(login_url='/login_admin/')
def add_task(request):
    deptdata=Department.objects.all()
    emp=Employee.objects.all()
    if request.method == 'POST':
        d = request.POST['departmentid']
        eid = request.POST['empid']
        p = request.POST['priority']
        t = request.POST['title']
        td = request.POST['description']
        eod = request.POST['eod']
        dept=Department.objects.get(id=d)
        em=Employee.objects.get(id=eid)
        Task.objects.create(dept=dept,emp=em,priority=p,title=t,description=td,endDate=eod,status='Not Updated Yet')
        messages.success(request, "Task Assign Successful")
        return redirect('admin_view_new_task')
    return render(request,'assign_task.html',locals())

def dropdown(request):
    data=Employee.objects.filter(dept__id=request.GET['deptid'])
    dict = {'id':[], 'name':[]}
    for i in data:
        dict['id'].append(i.id)
        dict['name'].append(i.user.first_name)
    return JsonResponse(dict)

def Login_Employee(request):
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        print(u)
        user = authenticate(username=u, password=p)
        sign = ""
        try:
            if user:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('emp_home')
        except:
            messages.success(request, "Invalid user")
    return render(request, 'emp_login.html')

def Logout(request):
    logout(request)
    return redirect('/')
@login_required(login_url='/login_emp/')
def emp_new_task(request):
    emp=Employee.objects.get(user=request.user)
    task=Task.objects.filter(emp=emp,status="Not Updated Yet")
    return render(request,'emp_new_task.html',locals())
@login_required(login_url='/login_emp/')
def emp_inprogress_task(request):
    emp=Employee.objects.get(user=request.user)
    task=Task.objects.filter(emp=emp,status="Inprogress")
    return render(request,'emp_inprogress_task.html',locals())
@login_required(login_url='/login_emp/')
def emp_completed_task(request):
    emp=Employee.objects.get(user=request.user)
    task=Task.objects.filter(emp=emp,status="Completed")
    return render(request,'emp_completed_task.html',locals())
@login_required(login_url='/login_emp/')
def emp_all_task(request):
    emp=Employee.objects.get(user=request.user)
    task=Task.objects.filter(emp=emp)
    return render(request,'emp_all_task.html',locals())
@login_required(login_url='/login_emp/')
def new_task_detail(request,pid):
    task=Task.objects.get(id=pid)
    tracker=TaskTracking.objects.filter(taskId=pid)
    return render(request,'new_task_detail.html',locals())
@login_required(login_url='/login_emp/')
def updateTaskTracker(request,pid):
    task = Task.objects.get(id=pid,emp__user=request.user)
    if request.method == "POST":
        r = request.POST['remark']
        s = request.POST['status']
        w = request.POST['workCompleted']
        task.remark=r
        task.status=s
        task.work=w
        task.save()
        TaskTracking.objects.create(taskId=task,remark=r,status=s,workCompleted=w)
        messages.success(request, "Remark Updated Successfully")
        return redirect('emp_new_task')
    return render(request,'update_task_tracker.html',locals())
@login_required(login_url='/login_emp/')
def Emp_Change_Password(request):
    user = User.objects.get(username=request.user.username)
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('emp_Change_Password')

    return render(request,'emp_change_password.html')
@login_required(login_url='/login_admin/')
def Admin_Change_Password(request):
    user = User.objects.get(username=request.user.username)
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('admin_Change_Password')

    return render(request,'admin_change_password.html')
@login_required(login_url='/login_admin/')
def admin_view_new_task(request):
    task=Task.objects.filter()
    return render(request,'admin_view_new_task.html',locals())
@login_required(login_url='/login_admin/')
def admin_view_inprogress_task(request):
    task=Task.objects.filter(status="Inprogress")
    return render(request,'admin_view_inprogress_task.html',locals())
@login_required(login_url='/login_admin/')
def admin_view_completed_task(request):
    task=Task.objects.filter(status="Completed")
    return render(request,'admin_view_completed_task.html',locals())
@login_required(login_url='/login_admin/')
def admin_view_task_detail(request,pid):
    task=Task.objects.get(id=pid)
    tracker=TaskTracking.objects.filter(taskId=pid)
    return render(request,'admin_view_task_detail.html',locals())
@login_required(login_url='/login_admin/')
def find_by_date(request):
    t=None
    datef=''
    datet=''
    if request.method=='POST':
        datef=request.POST['datef']
        datet=request.POST['datet']
        print(datef)
        print(datet)
        # try:
        t=Task.objects.filter(assignDate__date__lte=datet,assignDate__date__gte=datef)
        # except:
        #     t=None
        print(t)
    return render(request,'find_by_date.html',locals())
@login_required(login_url='/login_admin/')
def search_employee(request):
    data=""
    empId=""
    if request.method=='POST':
        empId=request.POST['empid']
        try:
            data=Employee.objects.get(empid=empId)
        except:
            data=None
    return render(request,'search_employee.html',locals())
@login_required(login_url='/login_admin/')
def view_emp_task(request,pid):
    emp=Employee.objects.get(id=pid)
    task=Task.objects.filter(emp=emp)
    return render(request,'view_emp_task_detail.html',locals())


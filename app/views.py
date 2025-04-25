from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.


def home(request):
    if request.method=='POST':
        empname=request.POST.get('empname')
        empid=request.POST.get('empid')
        empdept=request.POST.get('empdept')
        address=request.POST.get('Address')

        Employee.objects.create(
            Empname=empname,Empid=empid,Empdept=empdept,Address=address
        )
        return redirect('home')
    data=Employee.objects.all()
    return render(request,'home.html',{'data':data})



def view_emp(request):
    if request.method=='POST':
        empname=request.POST.get('empname')
        empid=request.POST.get('empid')
        empdept=request.POST.get('empdept')
        address=request.POST.get('Address')

        Employee.objects.create(
            Empname=empname,Empid=empid,Empdept=empdept,Address=address
        )
        return redirect('home')
    data=Employee.objects.all()
    return render(request,"home.html",{'data':data})


def edit_emp(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=='POST':
        emp.Empname=request.POST['empname']
        emp.Empid=request.POST['empid']
        emp.Empdept=request.POST['empdept']
        emp.Address=request.POST['Address']
        emp.save()
        return redirect('home')
    data=Employee.objects.all()
    return render(request,'home.html',{'emp':emp,'data':data})



def delete_emp(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('home')
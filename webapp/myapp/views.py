from django.shortcuts import render, redirect
from myapp.models import Employee
from myapp.forms import EmployeeForm

def home(request):
    return render(request, "index.html")

def load_form(request):
    form = EmployeeForm
    return render(request, "form.html", {'form': form})

def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect("/show")
    

def show(request):
    employee = Employee.objects.all
    return render(request, "show.html", {'employee': employee})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee': employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')

def search(request):
    given_name = request.POST['given_name']             #when i use ename there use many function like only ename, ename__iexact (not case sensetive) and ename__icontains (search minimun two letters)
    employee = Employee.objects.filter(ename__icontains=given_name)
    return render(request, "show.html", {'employee': employee})
    
    
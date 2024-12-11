from django.shortcuts import render
from .models import Employee, Department, Group

def index(request):
    groups = Group.objects.all().order_by('name')
    employees = Employee.objects.filter(status=1).order_by('lastname')
    

    
    context = { 
        'employees': employees,
        'groups': groups,
    }
    return render(request, 'info/index.html', context=context)
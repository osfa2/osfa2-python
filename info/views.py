import os
from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from datetime import datetime
from urllib.parse import urlparse, parse_qs

from .models import Employee, Department, Group, Link
from .osfa.OsfaFileBrowser import OsfaFileBrowser

def index(request):
    groups = Group.objects.all().order_by('name')
    employees = Employee.objects.filter(status=1).order_by('lastname')
    
    context = { 
        'employees': employees,
        'groups': groups,
    }
    return render(request, 'info/index.html', context=context)

def browser(request):
    file_browser = OsfaFileBrowser()
    list_of_objects = list()
    full_path = ""
    view_root_path = "docs/"
    view_base_path = "docs/"
    breadcrumbs = []

    if(request.method == "POST"):
        NUM_OF_PARTS_URL = 5
        click_type = request.POST['click_type']
        full_path = request.POST['full_path']
    
        parts_full_path = full_path.split('/')
        file_name = parts_full_path[-1:][0]
    
        parts_full_path_len = len(parts_full_path)
    
        #   we need a negative number to get the last items
        bc_indexes = parts_full_path_len - NUM_OF_PARTS_URL
        if bc_indexes > 0:
            breadcrumbs = parts_full_path[-abs(bc_indexes):]
            request.session['breadcrumbs'] = breadcrumbs
            view_base_path = view_root_path + '/'.join(breadcrumbs) + '/'
            
        if click_type == 'DIR':
            list_of_objects = file_browser.get_browser(full_path)
        else:
            with open(full_path,'rb') as doc:
                response = HttpResponse(doc.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = 'inline;filename=' + file_name
                return response
    else:
        # 'C:/inetpub/wwwosfa/static/docs/awarding_manual'
        breadcrumbs = request.session['breadcrumbs']
        absolute_url = request.build_absolute_uri()
        parsed_url = urlparse(absolute_url)
        parsed_qs = parse_qs(parsed_url.query)
        
        if len(parsed_qs) > 0:
            ordinal = int(parsed_qs['bc'][0])
            request.session['breadcrumbs'] = breadcrumbs[:ordinal+1]
            breadcrumbs = request.session['breadcrumbs']
            full_path = 'C:/inetpub/wwwosfa/static/docs/' + '/'.join(breadcrumbs)
        else:
            breadcrumbs = []
            request.session['breadcrumbs'] = []
                
        list_of_objects = file_browser.get_browser(full_path)
    
    list_of_objects.sort(key=lambda x: datetime.strptime(x.date_time, '%m/%d/%Y %I:%M:%S %p').timestamp(), reverse=True)
    list_of_objects.sort(key=lambda x: x.type, reverse=True)    
    
    context = {
        "file_objects": list_of_objects, 
        "breadcrumbs": breadcrumbs,
        "view_root_path": view_root_path,
        "view_base_path": view_base_path
    }
    
    return render(request, 'info/browser.html', context=context)

    
def approved_software(request):
    links = Link.objects.filter(linktype=1).order_by('displaytext')
    
    context = {
        'links': links
    }
    return render(request, 'info/approved_software.html', context=context)


def approved_usb(request):
    employees = Employee.objects.filter(approved_usb=1).order_by('nickname')
    
    context = {
        'employees': employees
    }
    return render(request, 'info/approved_usb.html', context=context)

def routing_slip(request):
    employees = Employee.objects.filter(status=1).filter(routingslip=1).order_by('group_id', 'lastname')
    group_ids = employees.values('group_id').distinct()
    groups = Group.objects.filter(id__in=group_ids).order_by('name')
    
    context = {
        'employees': employees,
        'groups': groups,
    }
    return render(request, 'info/routing_slip.html', context=context)

def routing_slip_preview(request):
    context = {}
    return render(request, 'info/routing_slip_preview.html', context=context)
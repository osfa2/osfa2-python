from django.shortcuts import render


def index(request):    
    context = { 
    }
    return render(request, 'app_inventory/index.html', context=context)
from django.shortcuts import render


def index(request):    
    context = { 
    }
    return render(request, 'app_workorder/index.html', context=context)
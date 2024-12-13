from django.shortcuts import render


def index(request):    
    context = { 
    }
    return render(request, 'app_leave/index.html', context=context)
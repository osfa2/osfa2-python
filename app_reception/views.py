from django.shortcuts import render


def index(request):    
    context = { 
    }
    return render(request, 'app_reception/index.html', context=context)
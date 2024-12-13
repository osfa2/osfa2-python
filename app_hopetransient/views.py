from django.shortcuts import render


def index(request):    
    context = { 
    }
    return render(request, 'app_hopetransient/index.html', context=context)
from django.shortcuts import render


def index(request):    
    context = { 
    }
    return render(request, 'app_formfinder/index.html', context=context)
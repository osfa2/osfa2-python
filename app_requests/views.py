from django.shortcuts import render


def index(request):    
    context = { 
    }
    return render(request, 'app_requests/index.html', context=context)

from django.shortcuts import render


def index(request):    
    context = { 
    }
    return render(request, 'app_formemail/index.html', context=context)
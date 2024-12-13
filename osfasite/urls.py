"""
URL configuration for osfasite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("/", include("info.urls")),
    path("info/", include("info.urls")),
    path("requests/", include("app_requests.urls")),
    path("ede/", include("app_ede.urls")),
    path("leave/", include("app_leave.urls")),
    path("mustread/", include("app_mustread.urls")),
    path("workorder/", include("app_workorder.urls")),
    path("formfinder/", include("app_formfinder.urls")),
    path("hopetransient/", include("app_hopetransient.urls")),  
    path("formemail/", include("app_formemail.urls")),
    path("reception/", include("app_reception.urls")),  
    path("inventory/", include("app_inventory.urls")),  
    path("employee/", include("app_employee.urls")), 
    path("admin/", admin.site.urls),
]

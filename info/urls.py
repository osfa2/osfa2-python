from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("browser", views.browser, name="browser"),
]
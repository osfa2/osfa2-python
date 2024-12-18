from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("browser", views.browser, name="browser"),
    path("approvedsoftware", views.approved_software, name="approved_software"),
    path("approvedusb", views.approved_usb, name="approved_usb"),
    path("routing/slip", views.routing_slip, name="routing_slip"),
    path('routing/slip/preview', views.routing_slip_preview, name='routing_slip_preview')
]
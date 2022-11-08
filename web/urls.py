from django.urls import path

from . import views

app_name="web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("service", views.service, name="service"),
    path("servicesingle", views.servicesingle, name="servicesingle"),
    path("updates", views.updates, name="updates"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("contact", views.contact, name="contact"),
    path("blogdetails", views.blogdetails, name="blogdetails"),
    path("enquiry", views.enquiry, name="enquiry"),
    
    
    
    
    ]

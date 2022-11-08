from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'web/index.html')


def about(request):
    return render(request,'web/about.html')    


def service(request):
    return render(request,'web/service.html')  

def servicesingle(request):
    return render(request,'web/servicesingle.html')


def updates(request):
    return render(request,'web/updates.html')  

def portfolio(request):
    return render(request,'web/portfolio.html')  



def contact(request):
    return render(request,'web/contact.html')  

def blogdetails(request):
    return render(request,'web/blogdetails.html') 


def enquiry(request):
    return render(request,'web/enquiry.html') 

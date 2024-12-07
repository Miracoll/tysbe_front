from django.shortcuts import render

# Create your views here.

def home(request):
    print(request.path)
    return render(request, 'page/index.html')

def service(request):
    print(request.path)
    return render(request, 'page/service.html')

def contact(request):
    print(request.path)
    return render(request, 'page/contact.html')

def faq(request):
    print(request.path)
    return render(request, 'page/faq.html')

def login(request):
    print(request.path)
    return render(request, 'page/login.html')
from django.shortcuts import render

# Create your views here.


def staticweb(request):
    return render(request, 'web/staticweb.html')


def ecommerceweb(request):
    return render(request, 'web/ecommerceweb.html')


def webredesign(request):
    return render(request, 'web/webredesign.html')


def customweb(request):
    return render(request, 'web/customweb.html')


def cmsbasedweb(request):
    return render(request, 'web/cmsbasedweb.html')


def pythondevelopment(request):
    return render(request, 'web/pythondevelopment.html')

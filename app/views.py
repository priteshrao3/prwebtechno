from django.shortcuts import render

# Create your views here.

def androidapp(request):
    return render(request, 'app/androidapp.html')


def iphoneapp(request):
    return render(request, 'app/iphoneapp.html')


def ipadapp(request):
    return render(request, 'app/ipadapp.html')


def hybridapp(request):
    return render(request, 'app/hybridapp.html')

from django.shortcuts import render

# Create your views here.

def seo(request):
    return render(request, 'seo/seo.html')


def localseo(request):
    return render(request, 'seo/localseo.html')


def linkbuilding(request):
    return render(request, 'seo/linkbuilding.html')


def contentwriting(request):
    return render(request, 'seo/contentwriting.html')


def ecommerceseo(request):
    return render(request, 'seo/ecommerceseo.html')


def emailmarketing(request):
    return render(request, 'seo/emailmarketing.html')


def ppc(request):
    return render(request, 'seo/ppc.html')


def aso(request):
    return render(request, 'seo/aso.html')



def smo(request):
    return render(request, 'seo/smo.html')

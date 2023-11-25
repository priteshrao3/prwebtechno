from django.shortcuts import render

# Create your views here.


def socialmedia(request):
    return render(request, 'sms/socialmedia.html')


def fbadvertising(request):
    return render(request, 'sms/fbadvertising.html')


def twittera(request):
    return render(request, 'sms/twittera.html')


def linkedina(request):
    return render(request, 'sms/linkedina.html')


def Instagramm(request):
    return render(request, 'sms/Instagramm.html')


def youtubem(request):
    return render(request, 'sms/youtubem.html')


def ormservices(request):
    return render(request, 'sms/ormservices.html')

from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail




# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def blog(request):
    return render(request, 'core/blog.html')


def portfolio(request):
    return render(request, 'core/portfolio.html')

def contact(request):
    fm = ContactForm
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if fm.is_valid():
            messages.success(request, 'Your Messege has been submited successfully')
            fm = ContactForm()
        else:
            fm = ContactForm()
        send_mail(
            subject,
            subject+'\n'+'\n'+ name +'\n'+'\n'+ email +'\n'+'\n'+ message,
            settings.EMAIL_HOST_USER,
            ['devloperpritesh@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'core/contact.html', {'form':fm})



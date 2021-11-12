from django.shortcuts import render
import random
from .models import package
# Create your views here.


def home(request):
    Package = package.objects.all()
    return render(request, 'lib/index.html', {"Package": Package})


def ss(request):
    Package = package.objects.all()
    passwordtypelist = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    length = int(request.GET.get('lenght', 12))
    if request.GET.get('uppercase'):
        passwordtypelist.extend('ABCBEFGHJKLMNOPQRSTVWXYZ')
    if request.GET.get('number'):
        passwordtypelist.extend('0123456789')
    if request.GET.get('special'):
        passwordtypelist.extend('!@#$%&()')
    for i in range(length):
        password += random.choice(passwordtypelist)

    return render(request, 'lib/secondscreen.html', {"Package": Package,
                                                     'password': password},)

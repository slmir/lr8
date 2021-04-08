from django.shortcuts import  render
from django.http import HttpResponse


def index(request):
    return render(request, 'icemaster/master.html')


def first_ice_cream(request):
    return render(request, 'icemaster/choco.html')


def second_ice_cream(request):
    return render(request, 'icemaster/vanil.html')


def third_ice_cream(request):
    return render(request, 'icemaster/cherry.html')
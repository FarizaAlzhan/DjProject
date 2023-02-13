from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect

from .models import *
# Create your views here.
def index(request):
    return render(request,'project/mainpage.html')

def training1(request):
    t1 = Training1.objects.all()
    t2 = Training1.objects.all()
    return render(request,'project/training1.html',{'t1':t1})
def training2(request):
    t2 = Training2.objects.all()
    return render(request,'project/training2.html',{'t2':t2})






def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')


def forbidden(request,exception):
    return HttpResponseForbidden('<h1>Доступ запрещен </h1>')


def serverError(exception):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')


def badRequest(request,exception):
    return HttpResponseBadRequest('<h1>Неверный запрос </h1>')

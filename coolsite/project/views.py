from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect

from .models import *
# Create your views here.
def index(request):
    return render(request,'project/mainpage.html')

def training1(request):
    t1 = Training1.objects.all()
    return render(request,'project/training1.html',{'t1':t1})
def training_manager1(request):
    tr1 = Training_manager1.objects.all()
    return render(request,'project/training_manager1.html',{'tr1':tr1})
def training2(request):
    t2 = Training2.objects.all()
    return render(request,'project/training2.html',{'t2':t2})
def books(request):
    b = Books.objects.all()
    categories = Category.objects.all()
    return render(request,'project/books.html',{'b':b,'categories': categories ,'category_selected':0 })

def show_category(request,category_id):
    b=Books.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'project/books.html', {'b': b, 'categories': categories, 'category_selected': category_id})


def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')


def forbidden(request,exception):
    return HttpResponseForbidden('<h1>Доступ запрещен </h1>')


def serverError(exception):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')


def badRequest(request,exception):
    return HttpResponseBadRequest('<h1>Неверный запрос </h1>')

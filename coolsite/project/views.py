from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("Страница проекта")

def categories(request,catid):
    return HttpResponse(f"<h1>Categories</h1><p>{catid}</p>")

def archive(request,year):
    if int(year)>2020:
        return redirect('home',permanent=True)
    return HttpResponse(f"<h1>Arhiv</h1><p>{year}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')


def forbidden(request,exception):
    return HttpResponseForbidden('<h1>Доступ запрещен </h1>')


def serverError(exception):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')


def badRequest(request,exception):
    return HttpResponseBadRequest('<h1>Неверный запрос </h1>')

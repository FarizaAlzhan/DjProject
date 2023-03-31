from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import *
from .forms import *
from .utils import *
from  django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request,'project/mainpage.html')

#@login_required
def aboutUs(request):
    return render(request,'project/aboutUs.html')

class Training1(ListView):
    model = Training1
    template_name = 'project/training1.html'
    allow_empty = False
# def training1(request):
#     t1 = Training1.objects.all()
#     return render(request,'project/training1.html',{'t1':t1})

def training_manager1(request):
    tr1 = Training_manager1.objects.all()
    tr2 = Training_manager2.objects.all()
    return render(request,'project/training_manager1.html',{'tr1':tr1,'tr2':tr2})
def training2(request):
    t2 = Training2.objects.all()
    return render(request,'project/training2.html',{'t2':t2})

class AllBooks(DataMixin,ListView):
    paginate_by = 3
    model = Books
    template_name = 'project/books.html'
    context_object_name = 'b'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Книги")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Books.objects.all().select_related('category')

# def books(request):
#     b = Books.objects.all()
#     return render(request,'project/books.html',{'b':b,'category_selected':0 })

class BooksCategory(DataMixin,ListView):
    model = Books
    template_name = 'project/books.html'
    context_object_name = 'b'

    def get_queryset(self):
        return Books.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
       ## c_def = self.get_user_context(title='Категория книг -' + str(context['b'][0].category),
           ##                           category_selected=context['b'][0].category_id)
        return context
            #dict(list(context.items()) + list(c_def.items()))

class AddTrainings1(LoginRequiredMixin, DataMixin,CreateView):
    form_class = AddTraining1Form
    template_name = 'project/addtraining1.html'
    success_url = reverse_lazy('training1')
    login_url = reverse_lazy('training1')

    #raise_exception = True
    def get_context_data(self,*,object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление тренинга")
        return dict(list(context.items()) + list(c_def.items()))

# def addtraining1(request):
#     if request.method == 'POST':
#         form = AddTraining1Form(request.POST,request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 # Training1.objects.create(**form.cleaned_data)
#                 form.save()
#
#                 return redirect('training1')
#             except:
#                 form.add_error(None,'Ошибка добавления тренинга')
#     else:
#         form = AddTraining1Form()
#     return render(request,'project/addtraining1.html', {'form': form})

class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'project/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*,object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('home')
class LoginUser(DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'project/login.html'

    def get_context_data(self,*,object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')


def forbidden(request,exception):
    return HttpResponseForbidden('<h1>Доступ запрещен </h1>')


def serverError(exception):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')


def badRequest(request,exception):
    return HttpResponseBadRequest('<h1>Неверный запрос </h1>')

from django.urls import path, re_path
from .views import *
urlpatterns = [

    path('',index,name='home'),
    path('training1/',training1),
    path('training2/',training2)


]
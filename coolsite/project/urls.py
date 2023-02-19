from django.urls import path, re_path
from .views import *
urlpatterns = [

    path('',index,name='home'),
    path('trainingSelfDevelopment/',training1,name='training1'),
    path('trainingPsychology',training2,name='training2'),
    path('books',books,name='books'),
    path('category/<int:category_id>/',show_category,name='category'),


]
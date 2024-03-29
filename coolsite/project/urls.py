from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *
urlpatterns = [

    path('',index,name='home'),
    path('trainingSelfDevelopment/',AllTraining1.as_view(),name='training1'),
    path('trainingManager1/',training_manager1,name='training_manager1'),
    path('trainingPsychology/',training2,name='training2'),
    path('books/',cache_page(60)(AllBooks.as_view()),name='books'),
    path('contact/',ContactFormView.as_view(),name='contact'),
    path('aboutUs/',aboutUs,name='aboutUs'),
    path('advice1',advice1,name='advice1'),
    path('advice2',advice2,name='advice2'),
    path('enroll',enroll,name='enroll'),
    path('motivation',motivation,name='motivation'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('addtraining1/', AddTrainings1.as_view(), name='addtraining1'),
    path('AddEnroll/', AddEnroll.as_view(), name='AddEnroll'),
    path('AllEnrolls/',AllEnroll,name='allEnroll'),
    path('Success/',Success,name='Success'),
    path('category/<slug:category_slug>/',cache_page(60)(BooksCategory.as_view()),name='category'),

    # path('post/<int:post_id>/',show_post,name='post'),


]
from django.urls import path, re_path
from .views import *
urlpatterns = [

    path('',index,name='home'),
    path('trainingSelfDevelopment/',Training1.as_view(),name='training1'),
    path('trainingManager1/',training_manager1,name='training_manager1'),
    path('trainingPsychology',training2,name='training2'),
    path('books',AllBooks.as_view(),name='books'),
    path('aboutUs',aboutUs,name='aboutUs'),
    path('addtraining1/', AddTrainings1.as_view(), name='addtraining1'),
    path('category/<slug:category_slug>/',BooksCategory.as_view( ),name='category'),

    # path('post/<int:post_id>/',show_post,name='post'),


]
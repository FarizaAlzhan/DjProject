"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin

from coolsite import settings
from project.views import *
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

from rest_framework import routers
# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get':'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix':'List'}),
#         routers.Route(url=r'{prefix}/{lookup}$',
#                       mapping={'get':'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix':'Detail'})
#     ]
router = routers.SimpleRouter()
# router.register(r'book',BookViewSet)
router.register(r'training1',Training1ViewSet)
router.register(r'training2',Training2ViewSet)
router.register(r'training_manager1',Training_manager1ViewSet)
router.register(r'training_manager2',Training_manager2ViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/',include('rest_framework.urls')),
    path('api/v1/auth/',include('djoser.urls')),
    re_path(r'^auth/',include('djoser.urls.authtoken')),
    path('api/v1/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/v1/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/v1/token/verify/',TokenVerifyView.as_view(),name='token_verify'),
    path('captcha/', include('captcha.urls')),
    path('',include('project.urls')),
    path('api/v1/',include(router.urls)),#http://127.0.0.1:8000/api/v1/training1/


    path('api/v1/book/',BookAPIList.as_view()),
    path('api/v1/bookcreate/',BookAPICreate.as_view()),
    path('api/v1/book/<int:pk>/',BookAPIUpdate.as_view()),
    path('api/v1/bookdelete/<int:pk>/',BookAPIDestroy.as_view()),



]
if settings.DEBUG:
   import debug_toolbar
   urlpatterns = [
       path('__debug__/', include(debug_toolbar.urls)),
   ] + urlpatterns
   urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound
handler403 = forbidden
handler500 = serverError
handler400 = badRequest
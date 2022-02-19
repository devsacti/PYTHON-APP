from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('templates1/', views.templatesAPI1, name='templates1'),

]
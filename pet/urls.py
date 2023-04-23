from django.urls import path

from pet import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),

]
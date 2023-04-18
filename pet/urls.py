from django.conf.urls import url

from pet import views

urlpatterns = [
    url('', views.pet, name='pet'),
]
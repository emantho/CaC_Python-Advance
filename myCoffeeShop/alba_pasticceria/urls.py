from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('sayHello/<str:userName>', views.sayHello, name='sayHello'),
    path('listName', views.listName, name='nameList'),
    path('abm_users', views.abm_users, name='abm_users'),
]

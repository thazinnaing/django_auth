from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('signin/', views.signup, name = 'signin'),
    path('show/', views.showdata, name = 'show')
]

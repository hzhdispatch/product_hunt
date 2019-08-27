from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.signup , name='注册页面'),
]

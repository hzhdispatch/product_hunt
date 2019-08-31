from django.urls import path
from . import views

urlpatterns = [
    path('publish/', views.publish, name='发布页面'),
]

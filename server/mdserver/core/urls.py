from django.urls import path

from . import views

urlpatterns = [
    path('articlelist', views.articlelist, name='articlelist'),
    path('login/', views.login, name = 'login'),
    # path('register/', views.register, name = 'register'),
    # path('is_login/', views.is_login, name = 'is_login'),
]
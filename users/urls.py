from django.urls import path

from . import views

urlpatterns = [
    path('guest_register/', views.guest_register_view, name='guest_register_view'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page')
]
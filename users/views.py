from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy


from .forms import MakeUserForm


class RegisterView(CreateView):
    form_class = MakeUserForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'
    
    
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UpdateUserView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    # fields = ['__all__']
    success_url = reverse_lazy('home')
    template_name = 'update.html'

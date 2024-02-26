from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')  # Adjusted the reverse_lazy call
    template_name = 'account/registrar.html'

    
# Create your views here.

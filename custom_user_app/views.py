from django.shortcuts import render
from custom_user_project.settings import AUTH_USER_MODEL
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def index(request):
    return render(request, 'home.html', {'model': AUTH_USER_MODEL})
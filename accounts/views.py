from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# def HomeView(request):
#     return HttpResponse("<h1>This is the Home Page...</h1>")

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/templates/register.html'
    success_url = reverse_lazy('login')
    
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request,*args,**kwargs)
    
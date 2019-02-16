from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import CustomUserForm

def index(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

class Signup(View):
    def get(self, request):
        form = CustomUserForm()
        return render(request, 'registration/signup.html', {'form': form})
    def post(self, request):
        form = CustomUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import CustomUserForm
from django.contrib.auth import authenticate

# def index(request):
#     user = request.user
#     return render(request, 'home.html', {'user': user})

# class Login(View):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'registration/login.html', {'form': form})

#     def post(self, request):
#         form = LoginForm(request.POST)
        
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user:
#             print('c')
#             return redirect('home')
#         return redirect('login')

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

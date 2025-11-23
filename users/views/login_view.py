import pyrebase
from django.views import View
from django.shortcuts import render, redirect
from django.conf import settings


class LoginView(View):
    config = settings.FIREBASE_CONFIG

    # database = firebase.database()
    def get(self, *args, **kwargs):
        return render(self.request, 'users/login.html')

    def post(self, *args, **kwargs):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        remember = self.request.POST.get('remember')
        return redirect('pdf:home-view')
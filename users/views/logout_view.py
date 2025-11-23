from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout

class LogoutView(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('pdf:home-view')
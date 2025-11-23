from django.views import View
from django.shortcuts import render

class RegisterView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'users/register.html')
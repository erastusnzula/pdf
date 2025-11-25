from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


class Register(View):
    def get(self, *args, **kwargs):
        form = UserCreationForm()
        context = {'form': form}
        return render(self.request, 'registration/register.html', context)

    def post(self, *args, **kwargs):
        form = UserCreationForm(data=self.request.POST)
        context = {'form': form}
        if form.is_valid():
            new_user = form.save()
            login(self.request, new_user)
            return redirect('pdf:home-view')
        return render(self.request, 'registration/register.html', context)

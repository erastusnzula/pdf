from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import ContactForm


class Register(View):
    def get(self, *args, **kwargs):
        form = UserCreationForm()
        context = {'form': form, 'message_success': True}
        return render(self.request, 'registration/register.html', context)

    def post(self, *args, **kwargs):
        form = UserCreationForm(data=self.request.POST)
        context = {'form': form}
        if form.is_valid():
            new_user = form.save()
            login(self.request, new_user)
            return redirect('pdf:home-view')
        return render(self.request, 'registration/register.html', context)

class ContactView(View):
    def get(self, *args, **kwargs):
        form = ContactForm()
        context = {'form': form}
        return render(self.request, 'accounts/contact.html', context)

    def post(self, *args, **kwargs):
        form = ContactForm(data=self.request.POST)
        new_form = ContactForm()
        context = {'form': form}
        if form.is_valid():
            form.save()
            return render(self.request, 'accounts/contact.html', {'form': new_form,'message': True})
        return render(self.request, 'accounts/contact.html', context)

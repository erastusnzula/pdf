import json

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from firebase_admin import auth as firebase_auth
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

class FirebaseConfig(View):
    def get(self, *args, **kwargs):
        return JsonResponse(settings.FIREBASE_CONFIG)

class FirebaseLogin(View):
    def post(self, *args, **kwargs):
        try:
            body = json.loads(self.request.body)
            id_token = body.get("idToken")

            decoded = firebase_auth.verify_id_token(id_token)
            email = decoded.get("email")
            uid = decoded.get("uid")
            name = decoded.get("name")

            # Create or get Django user
            user, created = User.objects.get_or_create(
                username=email,
                defaults={"first_name": name, "email": email}
            )

            login(self.request, user)
            return redirect('pdf:home-view')
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
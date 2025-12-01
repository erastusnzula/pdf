import os
import django
django.setup()
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
username = settings.username
email = settings.email
password = settings.password

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print('Superuser created')
    else:
        print('Superuser already exists')
else:
    print('Missing env vars for superuser')

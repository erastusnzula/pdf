from django.contrib.auth.models import User
from django.db import models


class AuthenticatedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_files")
    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdf files')
    date_created = models.DateTimeField(auto_now_add=True)
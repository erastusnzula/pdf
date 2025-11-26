from django import forms
from accounts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'message']
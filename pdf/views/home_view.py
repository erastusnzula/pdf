from django.views import View
from django.shortcuts import render

class HomeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/home_template.html')

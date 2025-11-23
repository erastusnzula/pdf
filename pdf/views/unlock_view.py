from django.views import View
from django.shortcuts import render, HttpResponse


class UnlockView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/unlock.html')

    def post(self, *args, **kwargs):
        return HttpResponse("Post")
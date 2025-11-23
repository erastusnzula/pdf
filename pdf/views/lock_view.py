from django.views import View
from django.shortcuts import render, HttpResponse


class LockView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/lock.html')

    def post(self, *args, **kwargs):
        return HttpResponse("Post")
from django.views import View
from django.shortcuts import render, HttpResponse

class CompressView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/compress.html')

    def post(self, *args, **kwargs):
        return HttpResponse("Post")
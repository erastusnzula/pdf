import os.path
import tempfile

from PyPDF2 import PdfReader, PdfWriter
from django.http import FileResponse
from django.views import View
from django.shortcuts import render, HttpResponse
from urllib3.filepost import writer


class LockView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/lock.html')

    def post(self, *args, **kwargs):
        pdf = self.request.FILES.get('pdf')
        password = self.request.POST.get('password')
        pdf_name = f"{os.path.splitext(pdf.name)[0]}_encrypted.pdf"
        reader = PdfReader(pdf)
        pdf_writer = PdfWriter()
        for page in reader.pages:
            pdf_writer.add_page(page)

        pdf_writer.encrypt(password)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        with open(temp_file.name, "wb") as f:
            pdf_writer.write(f)
        return FileResponse(open(temp_file.name, 'rb'), as_attachment=True, filename=pdf_name)
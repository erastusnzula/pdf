import io
import os
import tempfile

from PyPDF2 import PdfReader, PdfWriter
from django.http import FileResponse
from django.views import View
from django.shortcuts import render, HttpResponse


class UnlockView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/unlock.html')

    def post(self, *args, **kwargs):
        pdf  = self.request.FILES.get('pdf')
        password = self.request.POST.get('password')
        if not pdf:
            return HttpResponse("No file uploaded.", status=400)
        pdf_name = os.path.splitext(pdf.name)[0]
        try:
            reader = PdfReader(pdf)
            # If encrypted, try unlocking
            if reader.is_encrypted:
                result = reader.decrypt(password)
                if result == 0:  # Failed
                    return HttpResponse("Wrong password or unable to unlock this PDF.", status=400)
            # Create output writer
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)

            # Do NOT set a password => unlocked PDF
            output = io.BytesIO()
            writer.write(output)
            output.seek(0)

            new_filename = f"{pdf_name}_unlocked.pdf"
            response = HttpResponse(output, content_type="application/pdf")
            response["Content-Disposition"] = f'attachment; filename={new_filename}'
            return response
        except Exception as e:
            return HttpResponse(f"Error processing file: {str(e)}", status=400)
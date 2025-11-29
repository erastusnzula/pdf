import os

from django.views import View
from django.shortcuts import render, HttpResponse
from pikepdf import Pdf
import pikepdf
from django.conf import settings

class CompressView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/compress.html')

    def post(self, *args, **kwargs):
        pdf_file = self.request.FILES.get("pdf")

        if not pdf_file:
            return HttpResponse("No file uploaded", status=400)

        # Save input
        input_path = os.path.join(settings.BASE_DIR, pdf_file.name)
        with open(input_path, "wb+") as f:
            for chunk in pdf_file.chunks():
                f.write(chunk)

        # Output
        name, ext = os.path.splitext(pdf_file.name)
        output_name = f"{name}_compressed.pdf"
        output_path = os.path.join(settings.BASE_DIR, output_name)

        # Compress
        pdf = Pdf.open(input_path)
        pdf.save(output_path)
        pdf.close()

        # Return auto-download
        with open(output_path, "rb") as f:
            response = HttpResponse(f.read(), content_type="application/pdf")
            response["Content-Disposition"] = f"attachment; filename=" + output_name
            return response

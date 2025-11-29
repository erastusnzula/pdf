import os
import uuid

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from pdf2docx import Converter

TMP_DIR = os.path.join(os.getenv("TMP", "/tmp"))  # works on Windows and Linux


def pdf_to_docx(input_path, output_path, start=0, end=None):
    """
    Convert input_path PDF to output_path DOCX.
    start, end: 0-based page indexes (end is inclusive). Use None to convert till last page.
    """
    cv = Converter(input_path)
    try:
        cv.convert(output_path, start=start, end=end)  # convert whole file by default
    finally:
        cv.close()


class PdfToWord(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/pdf_to_word.html')

    def post(self, *args, **kwargs):
        upload = self.request.FILES.get("pdf")
        if not upload:
            return HttpResponse("No file uploaded", status=400)

        # Validate file extension quickly
        name, ext = os.path.splitext(upload.name)
        if ext.lower() not in [".pdf"]:
            return HttpResponse("Please upload a PDF file.", status=400)

        # Save upload to temp file
        uid = uuid.uuid4().hex
        input_path = os.path.join(TMP_DIR, f"{uid}_{upload.name}")
        with open(input_path, "wb+") as f:
            for chunk in upload.chunks():
                f.write(chunk)

        # Prepare output path
        output_name = f"{name}.docx"
        output_path = os.path.join(TMP_DIR, f"{uid}_{output_name}")

        try:
            # Convert (you can pass start, end pages if you want)
            pdf_to_docx(input_path, output_path)

            # Stream file back to user
            with open(output_path, "rb") as f:
                response = HttpResponse(f.read(),
                                        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                response["Content-Disposition"] = f'attachment; filename="{output_name}"'
                return response

        except Exception as e:
            # Log the error in real app; return friendly message
            return HttpResponse(f"Conversion failed: {str(e)}", status=500)

        finally:
            # Clean up temp files (best-effort)
            try:
                os.remove(input_path)
            except Exception:
                pass
            try:
                os.remove(output_path)
            except Exception:
                pass

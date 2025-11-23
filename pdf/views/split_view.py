import io
import os
import zipfile
from PyPDF2 import PdfReader, PdfWriter
from django.http import JsonResponse, FileResponse
from django.views import View
from django.shortcuts import render, HttpResponse


class SplitView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/split.html')

    def post(self, *args, **kwargs):
        file = self.request.FILES.get('pdf')
        if not file:
            return JsonResponse({"error": "No PDF uploaded"}, status=400)
        try:
            parts = int(self.request.POST.get('parts'))
            if parts < 2:
                return JsonResponse({"error": "Parts must be 2 or more"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Invalid parts value: {e}"}, status=400)
        reader = PdfReader(file)
        total_pages = len(reader.pages)
        pages_per_part = total_pages // parts
        remainder = total_pages % parts
        outputs = []
        start = 0
        for i in range(parts):
            writer = PdfWriter()
            end = start + pages_per_part + (1 if i < remainder else 0)
            for page_num in range(start, min(end, total_pages)):
                writer.add_page(reader.pages[page_num])
            # Save to memory buffer
            buffer = io.BytesIO()
            writer.write(buffer)
            buffer.seek(0)
            outputs.append(("part_" + str(i + 1) + ".pdf", buffer))
            start = end
        # Return ZIP containing all parts
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as z:
            for filename, pdf_buffer in outputs:
                z.writestr(filename, pdf_buffer.getvalue())
        zip_buffer.seek(0)
        return FileResponse(zip_buffer, as_attachment=True, filename="split_pdf.zip")
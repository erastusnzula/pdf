import io
import os

import fitz
from django.http import FileResponse
from django.views import View
from django.shortcuts import render


class MergeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pdf/merge.html')

    def post(self, *args, **kwargs):
        files = self.request.FILES.getlist('pdfs')
        files_names = []
        merged_pdf = fitz.open()
        try:
            for file in files:
                pdf = fitz.open(stream=file.read(), filetype='pdf')
                merged_pdf.insert_pdf(pdf)
                files_names.append(os.path.splitext(file.name)[0])
                pdf.close()
            output_name = "_".join(files_names)[:20] + "_merged.pdf"
            merged_file = io.BytesIO()
            merged_pdf.save(merged_file)
            merged_pdf.close()
            merged_file.seek(0)
            return FileResponse(merged_file, as_attachment=True, filename=output_name, content_type="application/pdf")
        except Exception as e:
            return render(self.request, 'pdf/merge.html', {"error": f"Error merging PDFs: {e}"})

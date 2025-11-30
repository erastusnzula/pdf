FROM python:3.11-slim

# Install Poppler (fixes PDFInfoNotInstalledError)
RUN apt-get update && \
    apt-get install -y poppler-utils && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Start Django with gunicorn
CMD ["gunicorn", " emuPDF.wsgi:application", "--bind", "0.0.0.0:8000"]

# Use an official Python runtime as a parent image
FROM python:3.11-slim


# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1


# Install OS-level deps (Poppler for pdf2image, build deps)
RUN apt-get update && \
apt-get install -y --no-install-recommends \
build-essential \
poppler-utils \
libjpeg-dev \
zlib1g-dev \
&& apt-get clean && rm -rf /var/lib/apt/lists/*


# Create app directory
WORKDIR /app


# Copy and install Python dependencies first (cache layer)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application
COPY . .


# Collect static files
ENV DJANGO_SETTINGS_MODULE=core.settings
RUN python manage.py collectstatic --noinput || true


# Expose port
EXPOSE 8000


# Start command (Render will use CMD or the Start Command set in the dashboard)
CMD ["gunicorn", "emuPDF.wsgi:application", "--bind", "0.0.0.0:8000"]

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (build-essential/gcc needed for some python packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port (Render sets PORT env)
ENV PORT=8000

# Command to run the application
CMD gunicorn app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:${PORT}

# -------- Base Image --------
FROM python:3.12-slim

# -------- Environment --------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# -------- Work Directory --------
WORKDIR /app

# -------- System Dependencies --------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
     curl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# -------- Install Python Dependencies --------
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# -------- Copy Application --------
COPY . .

# -------- Expose Port --------
EXPOSE 8000

# -------- Healthcheck (DevOps-safe) --------
# Socket-based check (no dependency on /health)
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=5 \
  CMD python -c "import socket; s=socket.socket(); s.settimeout(5); s.connect(('localhost',8000)); s.close()" || exit 1

# -------- Start Application --------
# Use uvicorn directly (more stable)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
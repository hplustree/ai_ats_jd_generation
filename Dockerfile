# Use official Python slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Copy requirements first for better cache handling
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full application
COPY . .

# Expose the port Uvicorn will run on
EXPOSE 9000

# Command to run the ASGI app
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "9000"]

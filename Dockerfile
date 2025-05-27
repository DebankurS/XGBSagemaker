# Start from official Python base
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install basic packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    build-essential \
    libgomp1 \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements-training.txt /opt/ml/code/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy training script
COPY train.py /opt/ml/code/train.py
ENV PYTHONPATH=/opt/ml/code

# Define entry point
ENTRYPOINT ["python", "/opt/ml/code/train.py"]

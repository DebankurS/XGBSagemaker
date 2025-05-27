FROM python:3.11

WORKDIR /code

# Install basic packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    build-essential \
    libgomp1 \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements-infer.txt /opt/ml/code/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /opt/ml/code/requirements.txt

COPY entrypoint.sh /usr/bin
COPY ./app /code/app

RUN chmod a+rx /usr/bin/entrypoint.sh

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]
FROM python:3.11-slim

WORKDIR /app

# System deps (git + certificates etc. are usually enough)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app", "--workers=1", "--threads=2", "--timeout=300"]

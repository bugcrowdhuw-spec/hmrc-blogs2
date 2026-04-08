# TaxPrep Dockerfile
# Multi-stage build for production deployment

FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

COPY taxprep/ /app/taxprep/
COPY data/ /app/data/
COPY config/ /app/config/
COPY skills/ /app/skills/

RUN mkdir -p /app/data/users /app/memory

RUN chmod +x /app/taxprep/cli.py || true

ENTRYPOINT ["python", "-m", "taxprep.cli"]
CMD ["--help"]
# =========================
# Stage 1 — Builder
# =========================
FROM python:3.12-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies (temporary)
RUN apk add --no-cache --virtual .build-deps \
    build-base linux-headers libffi-dev jpeg-dev zlib-dev postgresql-dev

# Copy requirements and install into a temporary directory
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt && \
    pip install --no-cache-dir --prefix=/install gunicorn

# =========================
# Stage 2 — Runtime
# =========================
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

# Only install runtime system dependencies
RUN apk add --no-cache libpq libjpeg zlib tini

# Copy dependencies from builder
COPY --from=builder /install /usr/local

# Copy Django project files
COPY . .

# Run migrations and collect static files
# Skip migrations if database doesn't exist, but always try collectstatic
RUN python manage.py migrate --noinput || true && \
    python manage.py collectstatic --noinput || true

# Expose port
EXPOSE ${PORT}

# Use Tini for proper signal handling
ENTRYPOINT ["/sbin/tini", "--"]

# Run gunicorn server
CMD ["sh", "-c", "gunicorn mysite.wsgi:application --bind 0.0.0.0:${PORT}"]

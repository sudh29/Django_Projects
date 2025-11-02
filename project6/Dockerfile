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

# Create non-root user and group first
RUN addgroup -S appgroup -g 1000 && \
    adduser -S appuser -G appgroup -u 1000 -h /app --no-create-home

# Create necessary directories with proper ownership
RUN mkdir -p /app/staticfiles /app/media /app/static && \
    chown -R appuser:appgroup /app && \
    chmod -R 755 /app

# Install system dependencies
RUN apk add --no-cache \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev \
    # Required for whitenoise
    zlib \
    libjpeg \
    libpng

# Expose port
EXPOSE ${PORT}

# Install whitenoise and other Python dependencies
RUN pip install --no-cache-dir whitenoise

# Set ownership again to ensure everything is owned by appuser
RUN chown -R appuser:appgroup /app && \
    chmod -R 755 /app

# Switch to non-root user
USER appuser

# Collect static files
RUN python manage.py collectstatic --noinput --clear

# Switch to non-root user
USER appuser

# Set the working directory
WORKDIR /app

# Use Tini for proper signal handling
ENTRYPOINT ["/sbin/tini", "--"]

# Run gunicorn server
CMD ["sh", "-c", "gunicorn blog.wsgi:application --bind 0.0.0.0:${PORT}"]

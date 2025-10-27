FROM python:3.12-slim-bullseye
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
WORKDIR /app

# Install uv
RUN pip install uv

# Copy and install dependencies
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt && uv pip install --system gunicorn

# Copy project files
COPY . .

# Expose port
EXPOSE ${PORT}

# Use shell form so ${PORT} expands correctly
CMD ["sh", "-c", "gunicorn core.wsgi:application --bind 0.0.0.0:${PORT}"]

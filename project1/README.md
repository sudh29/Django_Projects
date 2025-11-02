# 🎯 Django Project 1

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2.2-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16.0-red.svg)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📄 Description

A modern Django project template with a focus on best practices, security, and scalability. This project includes a complete REST API setup using Django REST Framework, JWT authentication, and separate development and production environments. Built with a multi-stage Docker configuration for optimal deployment and development workflows.

### Key Components

- **Django 5.2.2**: Latest stable Django release with enhanced security features
- **Django REST Framework 3.16.0**: Full REST API capabilities with SimpleJWT authentication
- **Multi-environment Setup**: Separate settings for development and production
- **Docker Support**: Multi-stage build process for minimal production image size
- **CORS Support**: Configured cross-origin resource sharing for API access

## ✨ Features

- � **JWT Authentication**: Secure API endpoints with JWT tokens
- 🌐 **REST API Ready**: Full DRF setup with browsable API interface
- �️ **CORS Enabled**: Configured for cross-origin requests
- 🐳 **Docker Optimized**: Multi-stage builds for minimal image size
- 🔒 **Environment-based Settings**: Development and production configurations
- � **Production-Ready**: Gunicorn server included for deployment
- � **API Documentation**: Built-in DRF documentation support

## 🔧 Requirements

- Python 3.12+
- Docker (optional, for containerized deployment)
- Git (optional, for version control)

## 🚀 Quick Start

### Local Development

1. **Clone and Set Up Environment**

   ```bash
   git clone <repository-url>
   cd project1
   python -m venv venv

   # On Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   # On Linux/WSL/macOS:
   source venv/bin/activate

   pip install -r requirements.txt
   ```

2. **Configure Environment**

   ```bash
   # Copy example environment file (if provided)
   cp .env.example .env  # Create this if needed

   # Initialize database
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

   - Admin Interface: http://127.0.0.1:8000/admin/
   - API Root: http://127.0.0.1:8000/api/
   - Documentation: http://127.0.0.1:8000/api/docs/

### Docker Deployment

```bash
# Build the Docker image
docker build -t django-project1 .

# Run the container
docker run -d -p 8080:8080 \
  --name django-project1 \
  -e DJANGO_SETTINGS_MODULE=core.settings.production \
  django-project1
```

## 📁 Project Structure

```
project1/
├── core/                # Main project configuration
│   ├── settings/       # Environment-specific settings
│   │   ├── __init__.py
│   │   ├── local.py    # Development settings
│   │   └── production.py# Production settings
│   ├── urls.py         # Main URL routing
│   ├── asgi.py         # ASGI configuration
│   └── wsgi.py         # WSGI configuration
├── myapp/              # Main application
│   ├── api/            # API endpoints
│   ├── models.py       # Database models
│   ├── serializers.py  # DRF serializers
│   ├── views.py        # View controllers
│   └── urls.py         # App URL patterns
├── Dockerfile          # Multi-stage Docker build
├── requirements.txt    # Python dependencies
└── manage.py          # Django CLI
```

## 🛠️ Development Commands

### Common Tasks

```bash
# Database Operations
python manage.py makemigrations  # Create migrations
python manage.py migrate         # Apply migrations
python manage.py createsuperuser # Create admin user

# Development Server
python manage.py runserver       # Run development server

# Testing
python manage.py test           # Run tests
coverage run manage.py test    # Run tests with coverage
coverage report               # View coverage report

# Create admin user
uv run python manage.py createsuperuser
```

### Package Management (uv)

```bash
# Install new package
uv pip install <package-name>

# Update requirements.txt
uv pip freeze > requirements.txt

# Sync virtual environment with requirements.txt
uv sync
```

### 🐳 Docker Setup and Commands

Before starting with Docker, ensure Docker is installed and running on your system. Visit [Docker's official website](https://docs.docker.com/get-docker/) for installation instructions.

#### Setting Up Docker

1. **Build the Image**

   - Uses multi-stage builds for optimization
   - Includes only production dependencies
   - Optimized for security and size

2. **Environment Variables**
   - Create a `.env` file based on `.env.example`
   - Never commit sensitive credentials to version control
   - Use different configurations for development and production

#### Common Docker Commands

```bash
# Build Docker image (use BuildKit for better performance)
docker build -t django-project1 .

# Run Docker container
docker run -d -p 8000:8080 \
  --env PIPELINE=local \
  --env SECRET_KEY=. \
  --env DB_NAME=. \
  --env DB_USER_NM=. \
  --env DB_USER_PW=. \
  --env DB_IP=0.0.0.0 \
  --env DB_PORT=5432 \
  --name django-app django-project1


http://localhost:8000/

# View container logs
docker logs django-app

# Stop container
docker stop django-app

# Remove container
docker rm django-app

docker images

docker rmi -f $(docker images -aq)
```

## 🧪 Testing and Quality

```bash
# Run tests
uv run python manage.py test

# Run tests with coverage
coverage run manage.py test
coverage report
```

## 🔑 Key URLs

- **Admin Interface**: http://127.0.0.1:8000/admin/
- **API Documentation**: http://127.0.0.1:8000/api/docs/ (if DRF is installed)
- **Main Application**: http://127.0.0.1:8000/

## 🛠️ Troubleshooting

### Common Issues

1. **Database Migrations**

   ```bash
   django.db.utils.OperationalError: no such table
   ```

   Solution: Run migrations

   ```bash
   python manage.py migrate
   ```

2. **Static Files Not Loading**

   - Check `STATIC_ROOT` in settings
   - Run `python manage.py collectstatic`
   - Verify your web server configuration

3. **Permission Issues with Docker**
   ```bash
   sudo usermod -aG docker $USER
   # Log out and log back in
   ```

### Debug Mode

- Set `DEBUG=True` only in development
- Use Django Debug Toolbar for development
- Monitor logs: `tail -f debug.log`

## 💡 Best Practices

1. **Code Style**

   - Follow PEP 8 guidelines
   - Use type hints
   - Write docstrings for functions/classes

2. **Security**

   - Keep `SECRET_KEY` secure
   - Use environment variables
   - Regular dependency updates
   - Enable HTTPS in production

3. **Testing**
   - Write tests for new features
   - Maintain good test coverage
   - Use factories for test data

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Security Best Practices](https://docs.djangoproject.com/en/stable/topics/security/)
- [Django Testing Guide](https://docs.djangoproject.com/en/stable/topics/testing/)
- [Docker Documentation](https://docs.docker.com/)

## 📈 Performance Optimization

### Database

- Use database indexes appropriately
- Implement caching where necessary
- Optimize querysets using `select_related()` and `prefetch_related()`

### Caching

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### Static Files

- Use CDN for production
- Compress and minify static files
- Implement lazy loading for images

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

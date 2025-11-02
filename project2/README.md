# 🎯 Django Forms Project

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2.2-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📄 Description

A Django project focused on demonstrating form handling and validation in Django web applications. This project includes examples of Django forms, form validation, template rendering, and form processing. Built with Docker support for easy deployment and development.

### Key Components

- **Django 5.2.2**: Latest stable Django release
- **Django Forms**: Complete form handling and validation
- **Templates**: Bootstrap-based form templates
- **Docker Support**: Containerized deployment ready
- **Basic App**: Example application showing forms implementation

## ✨ Features

- 📝 **Django Forms**: Complete form handling and validation
- � **Bootstrap Integration**: Beautiful form styling
- 🔍 **Form Validation**: Custom validation rules and error handling
- 🐳 **Docker Support**: Easy deployment with Docker
- 🔒 **CSRF Protection**: Built-in security for forms
- 📱 **Responsive Design**: Mobile-friendly form layouts
- 🎯 **Example Implementation**: Real-world form usage examples

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
docker build -t django-project2 .

# Run Docker container
docker run -d -p 8000:8000 \
  --name django-app2 \
  -e DJANGO_SETTINGS_MODULE=form.settings \
  django-project2
```

## 📁 Project Structure

```
project2/
├── form/               # Main project configuration
│   ├── settings.py    # Project settings
│   ├── urls.py        # Main URL routing
│   ├── asgi.py        # ASGI configuration
│   └── wsgi.py        # WSGI configuration
├── basicapp/          # Forms application
│   ├── forms.py       # Form definitions
│   ├── models.py      # Database models
│   ├── views.py       # View controllers
│   └── urls.py        # App URL patterns
├── templates/         # HTML templates
│   └── basicapp/     # App-specific templates
│       ├── form_page.html  # Form template
│       └── index.html      # Home page
├── Dockerfile         # Docker configuration
├── requirements.txt   # Python dependencies
└── manage.py         # Django CLI
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
docker build -t django-project2 .

# Run Docker container
docker run -d -p 8000:8080 --name django-app2 django-project2

http://localhost:8000/

# View container logs
docker logs django-app2

# Stop container
docker stop django-app2

# Remove container
docker rm django-app2

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
- **Form Page**: http://127.0.0.1:8000/form/
- **Home Page**: http://127.0.0.1:8000/

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

1. **Form Design**

   - Use appropriate form fields
   - Implement proper validation
   - Add helpful error messages
   - Use form widgets effectively

2. **Security**

   - Always use CSRF protection
   - Validate form data server-side
   - Sanitize user input
   - Use secure form submission

3. **User Experience**
   - Clear form labels and instructions
   - Responsive form layout
   - Proper error highlighting
   - Success/failure messages

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

# 🎯 Django Project 1

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-latest-green.svg)](https://www.djangoproject.com/)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-blueviolet)](https://astral.sh/uv/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern Django project template leveraging [uv](https://astral.sh/uv/) for lightning-fast Python package management and development workflow. This project follows best practices for Django development and includes a comprehensive setup for both local development and containerized deployment.

## ✨ Features

- 🚀 Lightning-fast dependency management with UV
- 🐳 Docker support for containerized deployment
- 🔒 Secure settings configuration
- 📊 Built-in testing and coverage setup
- 🎨 Modern project structure
- 📝 Comprehensive documentation

## 🔧 Requirements

- Python 3.12+
- [uv](https://astral.sh/uv/) - Modern Python package manager
- Git (optional, for version control)

## 🚀 Quick Start

1. **Clone and Navigate**

   ```bash
   git clone <repository-url>
   cd project1
   ```

2. **Set Up Development Environment**

   ```bash
   # Install uv (if not already installed)
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Create and activate virtual environment
   uv venv

   # On Linux/WSL/macOS:
   source .venv/bin/activate
   # On Windows PowerShell:
   .\.venv\Scripts\Activate.ps1

   # Install dependencies
   uv pip install -r requirements.txt
   ```

3. **Initialize Database**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

   Visit http://127.0.0.1:8000/ in your browser 🌐

## 📁 Project Structure

```
project1/
├── core/               # Main Django project configuration
│   ├── settings.py     # Project settings
│   ├── urls.py        # Main URL routing
│   └── wsgi.py        # WSGI configuration
├── myapp/             # Main application module
│   ├── models.py      # Database models
│   ├── views.py       # View controllers
│   └── urls.py        # App URL routing
├── manage.py          # Django management script
├── requirements.txt    # Project dependencies
└── db.sqlite3         # SQLite database
```

## 🛠️ Development Commands

### Essential Commands

```bash
# Create new app
python manage.py startapp <app_name>

# Generate database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
```

### Package Management

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

### Testing and Quality

```bash
# Run tests
python manage.py test

# Run tests with coverage
coverage run manage.py test
coverage report
```

## 🔑 Key URLs

- **Admin Interface**: http://127.0.0.1:8000/admin/
- **API Documentation**: http://127.0.0.1:8000/api/docs/ (if DRF is installed)
- **Main Application**: http://127.0.0.1:8000/

## � Troubleshooting

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

## Additional Resources

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

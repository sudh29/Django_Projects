# 🚀 Django Multi-App Project

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2.2-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.2-purple.svg)](https://getbootstrap.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Code Style](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📄 Description

A comprehensive Django project showcasing multi-app architecture with advanced form handling, template inheritance, and user management. This project demonstrates best practices in Django development including custom template tags, form validation, and responsive UI design using Bootstrap 5.

### Key Features

- **Multiple Django Apps**:
  - `firstapp`: Basic data display and manipulation
  - `twoapp`: Advanced form handling with custom validation
- **Template System**:
  - Custom template tags and filters
  - Bootstrap 5 responsive design
  - Modular template inheritance
- **Form Processing**:
  - Custom form validation
  - File upload handling
  - Interactive form UI with real-time feedback
- **Development Tools**:
  - Docker containerization
  - Development/Production settings separation
  - Static files management

## ✨ App Features

### First App (`firstapp`)

- � Data presentation and listing
- 🔄 Basic CRUD operations
- 📱 Responsive data tables
- 🎨 Bootstrap-styled interface

### Two App (`twoapp`)

- 📝 Advanced form processing with custom validation
- 🎨 Interactive form UI with real-time feedback
- 🔍 Custom template tags and filters
- 👥 User data management
- � Mobile-first responsive design

### Core Features

- 🎨 Bootstrap 5.3.2 integration
- 🔒 Built-in security features
- � Docker containerization
- 🔄 Sample data population scripts
- 📱 Responsive layouts across all pages

## 🔧 Requirements

- Python 3.12+
- Docker (optional, for containerized deployment)
- Git (optional, for version control)

## 🚀 Quick Start

### Local Development

1. **Set Up Python Environment**

   ```bash
   # Create and activate virtual environment
   python -m venv .venv

   # Windows PowerShell:
   .\.venv\Scripts\Activate.ps1
   # Linux/WSL/macOS:
   source .venv/bin/activate

   # Install dependencies
   python -m pip install -r requirements.txt
   ```

2. **Initialize Database**

   ```bash
   # Apply migrations
   python manage.py migrate

   # Create admin user
   python manage.py createsuperuser

   # Load sample data (optional)
   python populate_firstapp.py
   python populate_twoapp.py
   ```

3. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

   Visit these URLs in your browser:

   - Main Site: http://127.0.0.1:8000/
   - First App: http://127.0.0.1:8000/firstapp/
   - Forms Demo: http://127.0.0.1:8000/form/
   - User List: http://127.0.0.1:8000/user/
   - Admin Interface: http://127.0.0.1:8000/admin/

### Docker Deployment

```bash
# Build the Docker image
docker build -t django-project3 .

# Run the container
docker run -d -p 8000:8000 \
  --name django-project3 \
  -e DJANGO_SETTINGS_MODULE=Project3.settings \
  django-project3

# View logs
docker logs -f django-project3

# Stop and remove
docker stop django-project3
docker rm django-project3
```

### Development Tools

1. **Custom Template Tags**

   ```python
   # Load custom form filters
   {% load form_filters %}

   # Usage in templates
   {{ field|addclass:"form-control" }}
   ```

2. **Form Validation**

   ```python
   # Example from twoapp/form.py
   class UserForm(forms.ModelForm):
       class Meta:
           model = User
           fields = ['username', 'email', 'password']
   ```

3. **URL Configuration**
   ```python
   # Project3/urls.py routes
   path('firstapp/', include('firstapp.urls')),
   path('', include('twoapp.urls')),
   ```

## 📁 Project Structure

```
project3/
├── Project3/                # Main project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL routing
│   ├── asgi.py           # ASGI configuration
│   └── wsgi.py           # WSGI configuration
├── firstapp/              # First application
│   ├── models.py         # Database models
│   ├── views.py          # View controllers
│   ├── urls.py           # App URL patterns
│   └── migrations/       # Database migrations
├── twoapp/               # Advanced forms application
│   ├── form.py          # Form definitions
│   ├── models.py        # Database models
│   ├── views.py         # View controllers
│   ├── urls.py          # App URL patterns
│   └── templatetags/    # Custom template tags
│       └── form_filters.py  # Form-specific filters
├── templates/            # HTML templates
│   ├── home.html        # Main homepage
│   ├── firstapp/        # First app templates
│   │   └── index.html   # App index page
│   └── twoapp/          # Two app templates
│       ├── form.html    # Form handling page
│       ├── index.html   # App index page
│       └── user.html    # User management page
├── static/              # Static files
│   ├── css/            # Stylesheets
│   └── images/         # Image assets
├── Dockerfile          # Docker configuration
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
docker build -t django-project3 .

# Run Docker container
docker run -d -p 8000:8080 --name django-app3 django-project3

http://localhost:8000/

# View container logs
docker logs django-app3

# Stop container
docker stop django-app3

# Remove container
docker rm django-app3

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

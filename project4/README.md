# 🚀 Django Multi-App Project

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2.2-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.2-purple.svg)](https://getbootstrap.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Code Style](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📄 Description

A comprehensive Django project focused on user authentication and profile management. This project demonstrates best practices in Django development including user registration, login/logout functionality, custom user profiles, file uploads, and responsive UI design using Bootstrap 5.

### Key Features

- **User Authentication**:
  - User registration with profile extension
  - Secure login and logout functionality
  - Protected routes with `@login_required` decorator
- **Profile Management**:
  - Extended user profiles with portfolio site and profile pictures
  - Image upload handling for profile pictures
  - One-to-one relationship between User and UserProfileInfo
- **Template System**:
  - Custom template tags and filters (`form_filters`)
  - Bootstrap 5 responsive design
  - Modular template inheritance
- **Form Processing**:
  - Custom form validation with ModelForms
  - File upload handling (profile pictures)
  - Interactive form UI with real-time feedback
- **Development Tools**:
  - Docker containerization with multi-stage builds
  - REST Framework support (djangorestframework included)
  - Static and media files management

## ✨ App Features

### Login App (`login`)

- � Data presentation and listing
- 🔑 Secure user authentication (login/logout)
- 👤 Extended user profiles with portfolio and profile pictures
- 📝 Custom forms (UserForm and UserProfileInfoForm)
- 🎨 Bootstrap 5 styled forms with custom template filters
- 🛡️ Protected routes (special page requires authentication)
- 📤 Profile picture upload functionality

### Core Features

- 🎨 Bootstrap 5.3.2 integration
- 🔒 Built-in security features (CSRF protection, password hashing)
- 🎨 Interactive form UI with real-time feedback
- 🔍 Custom template tags and filters
- 👥 User data management
- � Mobile-first responsive design

### Core Features

- 🎨 Bootstrap 5.3.2 integration
- 🔒 Built-in security features
- � Docker containerization
- 🖼️ Media file handling (profile pictures)
- 📱 Responsive layouts across all pages
- 🔄 Django REST Framework support ready

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
   ```

3. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

   Visit these URLs in your browser:

   - Home Page: http://127.0.0.1:8000/
   - User Registration: http://127.0.0.1:8000/login/register/
   - User Login: http://127.0.0.1:8000/login/user_login/
   - Logout: http://127.0.0.1:8000/logout/
   - Special Page (Protected): http://127.0.0.1:8000/special/
   - Admin Interface: http://127.0.0.1:8000/admin/

### Docker Deployment

```bash
# Build the Docker image
docker build -t django-project4 .

# Run the container
docker run -d -p 8000:8080 \
  --name django-project4 \
  -e DJANGO_SETTINGS_MODULE=Project4.settings \
  django-project4

# View logs
docker logs -f django-project4

# Stop and remove
docker stop django-project4
docker rm django-project4
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
   # Example from login/forms.py
   class UserForm(forms.ModelForm):
       password = forms.CharField(widget=forms.PasswordInput())

       class Meta:
           model = User
           fields = ('username', 'email', 'password')

   class UserProfileInfoForm(forms.ModelForm):
       class Meta:
           model = UserProfileInfo
           fields = ('portfolio_site', 'porfile_pic')
   ```

3. **URL Configuration**
   ```python
   # Project4/urls.py routes
   path('', views.home, name='home'),
   path('login/', include('login.urls')),
   path('logout/', views.user_logout, name='logout'),
   path('special/', views.special, name='special'),  # Protected route
   ```

## 📁 Project Structure

```
project4/
├── Project4/                # Main project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL routing
│   ├── asgi.py           # ASGI configuration
│   └── wsgi.py           # WSGI configuration
├── login/                  # User authentication and profile app
│   ├── models.py         # UserProfileInfo model
│   ├── views.py          # View controllers (register, login, logout)
│   ├── forms.py          # UserForm and UserProfileInfoForm
│   ├── urls.py           # App URL patterns
│   ├── admin.py          # Admin configuration
│   ├── tests.py          # Unit tests
│   ├── migrations/       # Database migrations
│   └── templatetags/     # Custom template tags
│       └── form_filters.py  # Form-specific filters (addclass)
├── templates/            # HTML templates
│   ├── home.html        # Main homepage
│   └── login/           # Login app templates
│       ├── base.html    # Base template with Bootstrap
│       ├── login.html   # User login page
│       └── registration.html  # User registration page
├── media/               # User-uploaded files
│   └── profile_pics/     # Profile pictures
├── static/              # Static files
│   ├── css/            # Stylesheets (if any)
│   └── images/         # Image assets (if any)
├── Dockerfile          # Docker configuration (multi-stage build)
├── requirements.txt    # Python dependencies
├── .dockerignore       # Docker ignore patterns
├── db.sqlite3         # SQLite database
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
docker build -t django-project4 .

# Run Docker container
docker run -d -p 8000:8080 --name django-app4 django-project4

http://localhost:8000/

# View container logs
docker logs django-app4

# Stop container
docker stop django-app4

# Remove container
docker rm django-app4

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

- **Home Page**: http://127.0.0.1:8000/
- **User Registration**: http://127.0.0.1:8000/login/register/
- **User Login**: http://127.0.0.1:8000/login/user_login/
- **Logout**: http://127.0.0.1:8000/logout/
- **Special Page** (requires authentication): http://127.0.0.1:8000/special/
- **Admin Interface**: http://127.0.0.1:8000/admin/

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

   - Check `STATIC_ROOT` and `STATICFILES_DIRS` in settings
   - Run `python manage.py collectstatic` (for production)
   - Verify your web server configuration
   - Ensure `STATIC_URL = '/static/'` is set

3. **Media Files Not Uploading**

   - Check `MEDIA_ROOT` and `MEDIA_URL` in settings
   - Ensure media directory exists: `mkdir -p media/profile_pics`
   - Verify file permissions for media directory
   - In production, configure web server to serve media files

4. **Template Syntax Errors**

   - Ensure template tags are on separate lines
   - Check for matching `{% block %}` and `{% endblock %}` tags
   - Verify custom template tags are properly loaded: `{% load form_filters %}`

5. **Permission Issues with Docker**
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
   - Use password hashing (Argon2, BCrypt supported)
   - Protect sensitive routes with `@login_required`
   - Sanitize user input
   - Use secure form submission
   - Store uploaded files securely in `MEDIA_ROOT`

3. **User Experience**
   - Clear form labels and instructions
   - Responsive form layout
   - Proper error highlighting
   - Success/failure messages
   - Bootstrap 5 styling for modern UI
   - Custom template filters for consistent form styling

## 🔐 Authentication Features

This project implements a complete user authentication system:

- **User Registration**: Create new accounts with extended profile information
- **User Login**: Secure authentication using Django's built-in authentication system
- **User Logout**: Safe session termination
- **Profile Extension**: One-to-one relationship with additional fields (portfolio site, profile picture)
- **Protected Routes**: Use `@login_required` decorator to protect views
- **Password Security**: Uses Django's password hashing with multiple algorithms (Argon2, BCrypt, PBKDF2)

### Example: Protecting a View

```python
from django.contrib.auth.decorators import login_required

@login_required
def special(request):
    return HttpResponse("You are logged in")
```

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Authentication](https://docs.djangoproject.com/en/stable/topics/auth/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Security Best Practices](https://docs.djangoproject.com/en/stable/topics/security/)
- [Django Testing Guide](https://docs.djangoproject.com/en/stable/topics/testing/)
- [Docker Documentation](https://docs.docker.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)

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

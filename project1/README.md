# 🎯 Django Project 1

A modern Django project template leveraging [uv](https://astral.sh/uv/) for lightning-fast Python package management and development workflow.

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

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Django Rest Framework](https://www.django-rest-framework.org/) (if using DRF)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

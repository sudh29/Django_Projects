# 🐍 Django Projects Repository

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2.2-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16.0-red.svg)](https://www.django-rest-framework.org/)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-blueviolet)](https://astral.sh/uv/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive collection of Django projects demonstrating various functionalities, from basic setup to advanced REST APIs, authentication systems, and form handling. All projects use Python 3.12+ and modern development tools including [`uv`](https://astral.sh/uv/) for blazing-fast package management.

---

## 📑 Table of Contents

- [Projects Overview](#-projects-overview)
- [Quick Start](#-quick-start)
- [Environment Setup with UV](#️-environment-setup-with-uv)
- [Development Workflow](#️-development-workflow)
- [Repository Structure](#-repository-structure)
- [Tech Stack](#-tech-stack)
- [Docker Support](#-docker-support)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📁 Projects Overview

### 📌 [Project 1: Django REST API with JWT Authentication](project1/)

A modern Django project template with REST API setup using Django REST Framework and JWT authentication. Features multi-environment configuration and Docker support.

**Key Features:**
- Django REST Framework with SimpleJWT
- Multi-environment setup (dev/prod)
- Multi-stage Docker build
- CORS support

📄 **[View Full Documentation →](project1/README.md)**

---

### 📌 [Project 2: Django Forms & Validation](project2/)

Comprehensive demonstration of Django form handling, validation, and template rendering with Bootstrap-based UI.

**Key Features:**
- Django Forms with validation
- Bootstrap templates
- Form processing examples
- Docker deployment

📄 **[View Full Documentation →](project2/README.md)**

---

### 📌 [Project 3: Multi-App Architecture](project3/)

Advanced Django project showcasing multi-app architecture with custom template tags, form validation, and responsive UI.

**Key Features:**
- Multiple Django apps (firstapp, twoapp)
- Custom template tags and filters
- Bootstrap 5 responsive design
- Advanced form handling

📄 **[View Full Documentation →](project3/README.md)**

---

### 📌 [Project 4: User Authentication & Profile Management](project4/)

Complete user authentication system with profile management, file uploads, and protected routes.

**Key Features:**
- User registration and login
- Custom user profiles
- Profile picture uploads
- Protected routes with `@login_required`
- Bootstrap 5 UI

📄 **[View Full Documentation →](project4/README.md)**

---

### 📌 [Project 5: Advanced Authentication System](project5/)

Enhanced authentication project with extended user profile features and media file handling.

**Key Features:**
- Extended user profiles
- Media file management
- Secure authentication flow
- Responsive templates

📄 **[View Full Documentation →](project5/README.md)**

---

### 📌 [Project 6: Blog Application with REST API](project6/)

Feature-rich blog application with RESTful API, JWT authentication, posts, comments, and likes functionality.

**Key Features:**
- Complete blog REST API
- Post and Comment models
- Like/Unlike functionality
- JWT token authentication
- Comprehensive API documentation
- Docker & Docker Compose support

📄 **[View Full Documentation →](project6/README.md)**

---

## ⚡ Quick Start

Get started with any project in this repository in under 2 minutes:

```bash
# Clone the repository
git clone <repository-url>
cd Django_Projects

# Set up environment with UV
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install all dependencies
uv sync

# Navigate to any project
cd project6  # or project1, project2, etc.

# Run migrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser

# Start development server
uv run python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## ⚙️ Environment Setup with UV

[`uv`](https://astral.sh/uv/) is an extremely fast Python package installer and resolver, written in Rust. It's 10-100x faster than pip!

### 📦 Installing UV

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Using pip:**
```bash
pip install uv
```

### 🚀 Setting Up the Environment

#### 1. Create Virtual Environment
```bash
# Create a new virtual environment
uv venv

# Activate the environment
# Linux/macOS/WSL:
source .venv/bin/activate

# Windows PowerShell:
.venv\Scripts\Activate.ps1

# Windows CMD:
.venv\Scripts\activate.bat
```

#### 2. Install Dependencies

**Option A: Using pyproject.toml (Recommended)**
```bash
# Sync dependencies from pyproject.toml
uv sync
```

**Option B: Using requirements.txt**
```bash
# Install from requirements.txt
uv pip install -r requirements.txt
```

#### 3. Add New Packages
```bash
# Add a package and update pyproject.toml
uv add <package-name>

# Example:
uv add django-debug-toolbar

# Add a dev dependency
uv add --dev pytest
```

#### 4. Update Dependencies
```bash
# Update all packages
uv sync --upgrade

# Freeze current state to requirements.txt
uv pip freeze > requirements.txt
```

---

## 🛠️ Development Workflow

### Creating a New Django Project

```bash
# 1. Create project structure
uv run django-admin startproject myproject

# 2. Navigate to project
cd myproject

# 3. Create a Django app
uv run python manage.py startapp myapp

# 4. Add app to INSTALLED_APPS in settings.py
# Edit myproject/settings.py and add 'myapp' to INSTALLED_APPS
```

### Essential Django Commands

```bash
# Create migrations
uv run python manage.py makemigrations

# Apply migrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser

# Run development server
uv run python manage.py runserver

# Run on specific port
uv run python manage.py runserver 8080

# Access Django shell
uv run python manage.py shell

# Collect static files (production)
uv run python manage.py collectstatic

# Run tests
uv run python manage.py test
```

### Code Quality & Pre-commit Hooks

This repository uses pre-commit hooks for code quality:

```bash
# Install pre-commit hooks
pre-commit install

# Run on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files
pre-commit run flake8 --all-files
pre-commit run ruff --all-files
```

**Configured Tools:**
- **Black**: Code formatting
- **Flake8**: Linting
- **Ruff**: Fast Python linter
- **isort**: Import sorting

---

## 📂 Repository Structure

```
Django_Projects/
├── .venv/                      # Virtual environment (created by uv)
├── project1/                   # REST API with JWT
│   ├── core/                   # Project settings
│   ├── myapp/                  # Main application
│   ├── Dockerfile              # Docker configuration
│   ├── requirements.txt        # Project dependencies
│   └── README.md              # Project documentation
├── project2/                   # Forms & Validation
│   ├── form/                   # Project settings
│   ├── basicapp/              # Form application
│   └── README.md              # Project documentation
├── project3/                   # Multi-App Architecture
│   ├── Project3/              # Project settings
│   ├── firstapp/              # First application
│   ├── twoapp/                # Second application
│   └── README.md              # Project documentation
├── project4/                   # User Authentication
│   ├── Project4/              # Project settings
│   ├── login/                 # Authentication app
│   └── README.md              # Project documentation
├── project5/                   # Advanced Auth System
│   ├── mysite/                # Project settings
│   ├── home/                  # Home application
│   └── README.md              # Project documentation
├── project6/                   # Blog REST API
│   ├── blog/                  # Project settings
│   ├── blogapp/               # Blog application
│   ├── docker-compose.yml     # Docker Compose config
│   └── README.md              # Project documentation
├── .gitignore                 # Git ignore patterns
├── .pre-commit-config.yaml    # Pre-commit hooks config
├── .python-version            # Python version (3.12)
├── pyproject.toml             # UV project configuration
├── requirements.txt           # All dependencies
├── uv.lock                    # UV lock file
└── README.md                  # This file
```

---

## 🔧 Tech Stack

### Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.12+ | Programming language |
| **Django** | 5.2.2 | Web framework |
| **Django REST Framework** | 3.16.0 | REST API framework |
| **UV** | Latest | Package manager |

### Key Dependencies

**Authentication & Security:**
- `djangorestframework-simplejwt` (5.5.0) - JWT authentication
- `django-cors-headers` (4.7.0) - CORS support
- `pyjwt` (2.9.0) - JSON Web Tokens

**Development Tools:**
- `black` (25.1.0) - Code formatter
- `flake8` (7.2.0) - Linting
- `ruff` (0.11.13) - Fast Python linter
- `isort` (6.0.1) - Import sorting
- `pre-commit` (4.2.0) - Git hooks

**Data & Utilities:**
- `pandas` (2.3.0) - Data manipulation
- `numpy` (2.3.0) - Numerical computing
- `pillow` (12.0.0+) - Image processing
- `gunicorn` (23.0.0+) - WSGI server

**Full dependency list:** See [`requirements.txt`](requirements.txt) or [`pyproject.toml`](pyproject.toml)

---

## 🐳 Docker Support

Most projects include Docker and Docker Compose configurations for easy deployment.

### Using Docker

```bash
# Navigate to a project
cd project6

# Build the image
docker build -t django-project6 .

# Run the container
docker run -d -p 8000:8080 --name django-project6 django-project6

# View logs
docker logs -f django-project6

# Stop and remove
docker stop django-project6
docker rm django-project6
```

### Using Docker Compose

```bash
# Navigate to a project with docker-compose.yml
cd project6

# Start services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Execute commands in container
docker-compose exec web python manage.py createsuperuser

# Stop services
docker-compose down -v
```

**Projects with Docker Support:**
- ✅ Project 1 - Dockerfile
- ✅ Project 2 - Dockerfile
- ✅ Project 3 - Dockerfile
- ✅ Project 4 - Dockerfile
- ✅ Project 5 - Dockerfile
- ✅ Project 6 - Dockerfile + Docker Compose

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Getting Started

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/Django_Projects.git
   cd Django_Projects
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **Set up development environment**
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   pre-commit install
   ```

5. **Make your changes**
   - Follow existing code style
   - Add tests if applicable
   - Update documentation

6. **Run quality checks**
   ```bash
   pre-commit run --all-files
   uv run python manage.py test
   ```

7. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add amazing feature"
   ```

8. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

9. **Open a Pull Request**

### Code Style Guidelines

- Follow PEP 8 standards
- Use Black for code formatting
- Run Flake8 and Ruff for linting
- Write meaningful commit messages
- Add docstrings to functions and classes
- Keep functions small and focused

### Reporting Issues

Found a bug or have a suggestion? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version, etc.)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎓 Learning Resources

### Django Documentation
- [Official Django Docs](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

### UV Documentation
- [UV Official Docs](https://docs.astral.sh/uv/)
- [UV GitHub Repository](https://github.com/astral-sh/uv)

### Tutorials & Guides
- Each project includes detailed README with setup instructions
- Check individual project documentation for specific features
- Pre-commit hooks ensure code quality automatically

---

## 📊 Project Statistics

- **Total Projects:** 6
- **Python Version:** 3.12+
- **Django Version:** 5.2.2
- **Total Dependencies:** 36+
- **Docker Support:** All projects
- **Code Quality Tools:** Black, Flake8, Ruff, isort

---

## 🙏 Acknowledgments

- Django Software Foundation for the amazing framework
- Astral for creating UV - the blazing fast package manager
- All contributors and the open-source community

---

## 📞 Support

For questions or support:
- Open an issue on GitHub
- Check individual project READMEs
- Review Django documentation

---

**Built with ❤️ using Django, DRF, and UV**

*Last Updated: November 2024*

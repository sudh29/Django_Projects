# 🐍 Django Projects Repository

This repository contains multiple Django-based projects demonstrating different functionalities and use cases using Python 3.12+ and [`uv`](https://astral.sh/uv/) for modern package management.

---

## 📁 Projects Overview

### 📌 Project 1: Basic Django Setup
A foundational Django project to demonstrate initial setup, app creation, and Django admin interface.

- 📄 [View README for Project 1](project1/README.md)

---

### 📌 Project 2: CRUD API with Django REST Framework
This project demonstrates CRUD (Create, Read, Update, Delete) operations using Django REST Framework.

- 📄 [View README for Project 2](project2/README.md)

---

## ⚙️ Setup & Development Guide

A step-by-step guide to set up and run Django projects using [`uv`](https://astral.sh/uv/), a blazing fast Python package manager.

### ✅ Requirements

- Python 3.12+
- [`uv`](https://astral.sh/uv/) (virtual environment and package management tool)

---

### 🚀 Getting Started

#### 1. Install `uv`
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a virtual environment
```bash
uv venv
```

3. Activate the virtual environment
```bash
source .venv/bin/activate
```

4. Install project dependencies
```bash
uv pip install -r requirements.txt
```

Alternatively:
```bash
uv sync
```

5. (Optional) Freeze current dependencies
```bash
uv pip freeze > requirements.txt
```

🛠️ Django Project Initialization
If you haven't created a Django project yet:

6. Start a new Django project
```bash
uv run django-admin startproject <project_name>
```

7. Create a Django app (inside your project)
```bash
uv run python manage.py startapp <app_name>
```

📌 Essential Commands
8. Apply migrations
```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

9. Create a superuser
```bash
uv run python manage.py createsuperuser
```

🔍 Code Quality & Pre-commit Hooks
10. Install pre-commit hooks
```bash
pre-commit install
```

11. Run pre-commit on all files
```bash
pre-commit run --all-files
```

▶️ Run the Development Server
12. Start the Django development server
```bash
uv run python manage.py runserver
```

Then visit: http://127.0.0.1:8000/

########################################################

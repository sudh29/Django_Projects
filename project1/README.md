# Django Project 1

A simple Django project setup guide using [uv](https://astral.sh/uv/) for fast Python package management.

## Requirements
- Python 3.12+
- [uv](https://astral.sh/uv/) (for virtual environment and dependency management)

## Setup Instructions

1. **Install uv**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. **Create a virtual environment**
   ```bash
   uv venv
   ```
3. **Activate the virtual environment**
   ```bash
   source .venv/bin/activate
   ```
4. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```
5. **Start a new Django project (if not already created)**
   ```bash
   django-admin startproject core .
   ```
6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Create a new Django app (optional)**
   ```bash
   python manage.py startapp myapp
   ```


## Additional Notes
- The default Django app is located in the `core/` directory.
- The database file is `db.sqlite3`.
- To install new packages, use `uv pip install <package>`.

## Useful Commands
- Run migrations:
  ```bash
  python manage.py migrate
  ```
- Create a superuser:
  ```bash
  python manage.py createsuperuser
  ```

# 📝 Django Blog Application

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2.2-green.svg)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.16.0-red.svg)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A feature-rich Django blog application with a RESTful API built using Django REST Framework. This project demonstrates a complete blogging platform with JWT authentication, post management, comments, and likes functionality.

## ⚡ Quick Start

```bash
# Clone and setup
git clone <repository-url>
cd project6

# Using Docker Compose (Recommended)
docker-compose up -d --build

# OR using local development
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Access at http://localhost:8000/
```

## 📑 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Getting Started](#-getting-started)
  - [Local Development Setup](#-local-development-setup)
  - [Docker Deployment](#-docker-deployment)
- [Authentication](#-authentication)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Key Models](#-key-models)
- [Testing](#-testing)
- [Production Deployment](#-production-deployment)
- [Usage Examples](#-usage-examples)
- [Dependencies](#-dependencies)

## 🎯 Features

### Core Features
- **User Authentication**
  - JWT-based authentication using Simple JWT
  - Token obtain and refresh endpoints
  - Secure user authentication

### Blog Management
- **Posts**
  - Create, read, update, and delete blog posts
  - Author attribution with ForeignKey to User
  - Auto-generated timestamps (published_date)
  - Like functionality with ManyToMany relationship

### Engagement
- **Comments**
  - Add and manage comments on posts
  - Author tracking for each comment
  - Timestamps for comment creation
- **Likes**
  - Like/unlike posts
  - Like count tracking via ManyToMany field

### API Features
- RESTful API endpoints
- JWT Authentication with djangorestframework-simplejwt
- IsAuthenticatedOrReadOnly permissions
- CORS support with django-cors-headers

### Admin Features
- Django admin interface
- User management
- Post and comment moderation

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- pip (Python package manager)
- [Git](https://git-scm.com/)
- (Optional) [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- (Optional) [PostgreSQL](https://www.postgresql.org/) (production)

### 🛠 Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd project6
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Linux/macOS/WSL
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows PowerShell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin) account**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at:
- **Home/API**: http://127.0.0.1:8000/
- **Admin Interface**: http://127.0.0.1:8000/admin/
- **API Endpoints**: http://127.0.0.1:8000/api/
- **JWT Token**: http://127.0.0.1:8000/api/token/

---

## 🐳 Docker Deployment

### Option 1: Using Docker (Standard)

**Build the Docker image:**
```bash
docker build -t django-blog-app .
```

**Run the container:**
```bash
docker run -d -p 8000:8080 \
  --name django-blog-app \
  -e DJANGO_SETTINGS_MODULE=blog.settings \
  django-blog-app
```

**Access the application:**
- Application: http://localhost:8000/
- Admin: http://localhost:8000/admin/

**View logs:**
```bash
docker logs -f django-blog-app
```

**Stop and remove container:**
```bash
docker stop django-blog-app
docker rm django-blog-app
```

### Option 2: Using Docker Compose (Recommended)

**Start the application:**
```bash
# Build and start containers in detached mode
docker-compose up -d --build
```

**Access the application:**
- Application: http://localhost:8000/
- Admin: http://localhost:8000/admin/

**View logs:**
```bash
# Follow logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f web
```

**Stop the application:**
```bash
# Stop containers
docker-compose stop

# Stop and remove containers, networks, and volumes
docker-compose down -v
```

**Rebuild after code changes:**
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

**Execute commands in running container:**
```bash
# Create superuser
docker-compose exec web python manage.py createsuperuser

# Run migrations
docker-compose exec web python manage.py migrate

# Access Django shell
docker-compose exec web python manage.py shell
```

### Docker Configuration Details

**Dockerfile Features:**
- Multi-stage build for smaller image size
- Python 3.12 Alpine base image
- Non-root user execution (UID/GID 1000)
- Gunicorn WSGI server on port 8080
- WhiteNoise for static file serving
- Tini for proper signal handling

**Docker Compose Features:**
- Automatic migrations on startup
- Static file collection on startup
- Named volumes for persistent data
- Health check endpoint configuration
- Environment variable configuration
- Port mapping: 8000 (host) → 8080 (container)

**Important Notes:**
- The container exposes port **8080** internally
- Port **8000** on your host machine maps to container port 8080
- Database is SQLite (stored in mounted volume)
- Static files are collected automatically on container start
- For production, consider using PostgreSQL instead of SQLite

---

## 🔐 Authentication

This API uses **JWT (JSON Web Token)** authentication. To access protected endpoints:

1. **Obtain Access Token**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
   ```

   Response:
   ```json
   {
     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
     "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
   }
   ```

2. **Use Access Token in API Requests**
   ```bash
   curl -X GET http://127.0.0.1:8000/api/posts/ \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
   ```

3. **Refresh Access Token** (when expired)
   ```bash
   curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
     -H "Content-Type: application/json" \
     -d '{"refresh": "YOUR_REFRESH_TOKEN"}'
   ```

## 📚 API Documentation

The API follows RESTful design principles and uses JWT for authentication. Endpoints are available at both root (`/`) and `/api/` prefixes.

### 🔐 Authentication Endpoints

#### 1. Obtain JWT Token

**Endpoint:** `POST /api/token/`

**Request:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response (200 OK):**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Description:**
- Obtain JWT access and refresh tokens for authentication
- Access token for API requests
- Refresh token to obtain new access tokens

#### 2. Refresh JWT Token

**Endpoint:** `POST /api/token/refresh/`

**Request:**
```json
{
  "refresh": "your_refresh_token"
}
```

**Response (200 OK):**
```json
{
  "access": "new_access_token"
}
```

**Description:**
- Get a new access token when the current one expires
- Requires a valid refresh token

### 📝 Post Endpoints

#### List All Posts

**Endpoint:** `GET /api/posts/` or `GET /posts/`

**Authentication:** Optional (read-only without authentication)

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is the content...",
    "author": "username",
    "published_date": "2024-01-15T10:30:00Z",
    "likes_count": 5,
    "comments": [
      {
        "id": 1,
        "author": "commenter",
        "text": "Great post!",
        "created_date": "2024-01-15T11:00:00Z"
      }
    ]
  }
]
```

#### Create a Post

**Endpoint:** `POST /api/posts/` or `POST /posts/`

**Authentication:** Required (JWT Bearer token)

**Request:**
```json
{
  "title": "My New Post",
  "content": "This is the post content..."
}
```

**Response (201 Created):**
```json
{
  "id": 2,
  "title": "My New Post",
  "content": "This is the post content...",
  "author": "username",
  "published_date": "2024-01-15T12:00:00Z",
  "likes_count": 0,
  "comments": []
}
```

#### Retrieve a Post

**Endpoint:** `GET /api/posts/{id}/` or `GET /posts/{id}/`

**Authentication:** Not required

**Response (200 OK):** Same as individual post object above

#### Update a Post

**Endpoint:** `PUT /api/posts/{id}/` or `PATCH /api/posts/{id}/`

**Authentication:** Required (must be post author)

**Request:**
```json
{
  "title": "Updated Title",
  "content": "Updated content..."
}
```

**Response (200 OK):** Updated post object

#### Delete a Post

**Endpoint:** `DELETE /api/posts/{id}/`

**Authentication:** Required (must be post author)

**Response (204 No Content)**

#### Like/Unlike a Post

**Endpoint:** `POST /api/posts/{id}/like/` or `POST /posts/{id}/like/`

**Authentication:** Required

**Response (200 OK):**
```json
{
  "liked": true,
  "likes_count": 6
}
```

**Description:** Toggles like status - adds like if not liked, removes if already liked

### 💬 Comment Endpoints

#### List Comments for a Post

**Endpoint:** `GET /api/posts/{post_id}/comments/` or `GET /posts/{post_id}/comments/`

**Authentication:** Not required

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "author": "commenter",
    "text": "Great post!",
    "created_date": "2024-01-15T11:00:00Z"
  }
]
```

#### Create a Comment

**Endpoint:** `POST /api/posts/{post_id}/comments/` or `POST /posts/{post_id}/comments/`

**Authentication:** Required

**Request:**
```json
{
  "text": "This is my comment"
}
```

**Response (201 Created):**
```json
{
  "id": 3,
  "author": "username",
  "text": "This is my comment",
  "created_date": "2024-01-15T12:00:00Z"
}
```

#### Delete a Comment

**Endpoint:** `DELETE /api/posts/{post_id}/comments/{id}/` or `DELETE /posts/{post_id}/comments/{id}/`

**Authentication:** Required (must be comment author)

**Response (204 No Content)**

## 🧪 Testing

Run the test suite with:

```bash
python manage.py test
```

Or with coverage:

```bash
coverage run manage.py test
coverage report
```

## 🚀 Production Deployment

### Production Checklist
1. Set `DEBUG=False` in settings
2. Configure a production database (PostgreSQL recommended)
3. Set up proper web server (Nginx + Gunicorn)
4. Configure HTTPS with Let's Encrypt
5. Set up proper logging and monitoring
6. Use environment variables for sensitive data
7. Enable WhiteNoise for static files (already configured)

### Docker Production Configuration

The Dockerfile uses a multi-stage build for optimized production images:
- **Stage 1 (Builder)**: Installs dependencies
- **Stage 2 (Runtime)**: Creates minimal production image with:
  - Non-root user (appuser:appgroup)
  - Gunicorn WSGI server
  - WhiteNoise for static file serving
  - Tini for proper signal handling
  - Optimized Alpine Linux base

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django REST Framework for the amazing API framework
- Simple JWT for JWT authentication
- All contributors who helped improve this project

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

### Test Coverage

The test suite includes:
- ✅ Post model tests
- ✅ Comment model tests
- ✅ Post API tests (CRUD operations)
- ✅ Comment API tests (Create, List, Delete)
- ✅ Authentication tests
- ✅ Permission tests (author-only updates/deletes)
- ✅ Pagination tests

### Example Test Output
```
test_create_post (blogapp.tests.PostAPITest) ... ok
test_list_posts (blogapp.tests.PostAPITest) ... ok
test_retrieve_post (blogapp.tests.PostAPITest) ... ok
test_update_post (blogapp.tests.PostAPITest) ... ok
test_delete_post (blogapp.tests.PostAPITest) ... ok
test_author_can_update_own_post (blogapp.tests.PostAPITest) ... ok
test_other_user_cannot_update_post (blogapp.tests.PostAPITest) ... ok
test_pagination (blogapp.tests.PostAPITest) ... ok
test_comment_str (blogapp.tests.CommentModelTest) ... ok
test_create_comment (blogapp.tests.CommentAPITest) ... ok
test_delete_comment (blogapp.tests.CommentAPITest) ... ok

----------------------------------------------------------------------
Ran 11 tests in X.XXXs

OK
```

## 📁 Project Structure

```
project6/
├── blog/                       # Main project configuration
│   ├── __init__.py
│   ├── settings.py            # Django settings with JWT & CORS config
│   ├── urls.py                # Root URL configuration with JWT endpoints
│   ├── wsgi.py                # WSGI configuration for deployment
│   └── asgi.py                # ASGI configuration
├── blogapp/                    # Blog application
│   ├── models.py              # Post and Comment models
│   ├── views.py               # API ViewSets
│   ├── serializers.py         # DRF serializers
│   ├── urls.py                # App URL patterns
│   ├── admin.py               # Admin configuration
│   ├── tests.py               # Unit tests
│   ├── migrations/            # Database migrations
│   ├── static/                # App-specific static files
│   └── templates/             # App templates
├── static/                     # Project-wide static files
├── staticfiles/                # Collected static files (production)
├── media/                      # User-uploaded media files
├── Dockerfile                  # Multi-stage Docker build configuration
├── docker-compose.yml          # Docker Compose configuration
├── .dockerignore               # Docker ignore patterns
├── requirements.txt            # Python dependencies
├── manage.py                   # Django management CLI
├── db.sqlite3                  # SQLite database (development)
└── README.md                   # This file
```

## 🔑 Key Models

### Post Model
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
```

**Fields:**
- `title`: Post title (max 200 characters)
- `content`: Post content (unlimited text)
- `author`: ForeignKey to User (post creator)
- `published_date`: Auto-generated timestamp on creation
- `likes`: ManyToMany relationship with User for like functionality

### Comment Model
```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
```

**Fields:**
- `post`: ForeignKey to Post (parent post)
- `author`: ForeignKey to User (comment creator)
- `text`: Comment content (unlimited text)
- `created_date`: Timestamp with default to current time

## 🔒 Security & Configuration

### Security Features
- **JWT Authentication**: Token-based authentication using djangorestframework-simplejwt
- **Permission Classes**: `IsAuthenticatedOrReadOnly` - read access for all, write access for authenticated users
- **Author Permissions**: Only post/comment authors can update/delete their content
- **CORS Enabled**: Cross-Origin Resource Sharing configured with django-cors-headers
- **CSRF Protection**: Django's built-in CSRF protection
- **Password Hashing**: Secure password hashing with Django's authentication system
- **Non-root Docker User**: Container runs as `appuser` (UID 1000) for security

### Static Files Configuration
- **WhiteNoise**: Efficient static file serving in production
- **CompressedManifestStaticFilesStorage**: Automatic compression and caching
- **Static Root**: `/app/staticfiles` for collected static files
- **Media Root**: `/app/media` for user uploads

## 💡 Usage Examples

### Using curl

#### Create a Post
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My New Post",
    "content": "This is the content of my new post."
  }'
```

#### Create a Comment
```bash
curl -X POST http://127.0.0.1:8000/api/posts/1/comments/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Great post! Thanks for sharing."
  }'
```

#### Like a Post (Bonus Feature)
Note: Like functionality can be implemented via the admin interface or by adding a custom endpoint.

### Using Python requests

```python
import requests

# Get token
response = requests.post('http://127.0.0.1:8000/api/token/', json={
    'username': 'your_username',
    'password': 'your_password'
})
token = response.json()['access']

# Create a post
headers = {'Authorization': f'Bearer {token}'}
response = requests.post(
    'http://127.0.0.1:8000/api/posts/',
    headers=headers,
    json={
        'title': 'My Post',
        'content': 'Post content here'
    }
)
print(response.json())
```

## 🛠️ Development Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Access Django shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic
```

## 📚 Dependencies

Core dependencies as defined in `requirements.txt`:

- **Django 5.2.2**: Web framework
- **djangorestframework 3.16.0**: REST API framework
- **djangorestframework-simplejwt 5.5.0**: JWT authentication
- **django-cors-headers 4.7.0**: CORS handling
- **gunicorn 23.0.0**: Production WSGI server
- **whitenoise**: Static file serving (installed in Docker)
- **asgiref 3.8.1**: ASGI support
- **sqlparse 0.5.3**: SQL parsing
- **tzdata 2025.2**: Timezone data

## 🎯 Assignment Requirements Checklist

- ✅ **Models**: Post and Comment models with all required fields
- ✅ **APIs**: Full CRUD for Posts, List/Create/Delete for Comments
- ✅ **Views and URLs**: All endpoints properly configured
- ✅ **Authentication**: JWT token-based authentication
- ✅ **Authorization**: Authenticated users can create/modify, authors only for updates/deletes
- ✅ **Documentation**: Comprehensive README with API documentation
- ✅ **Testing**: Tests for models and API views
- ✅ **Bonus**: Pagination and Like functionality implemented

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 📞 Support

For questions or issues, please open an issue on the GitHub repository.

---

## 🎓 Project Summary

This Django blog application demonstrates:

✅ **RESTful API Design** - Clean, well-structured API endpoints
✅ **JWT Authentication** - Secure token-based authentication
✅ **Django Best Practices** - Proper model relationships, serializers, and views
✅ **Docker Deployment** - Production-ready containerization with multi-stage builds
✅ **Security** - Non-root containers, CORS, authentication, and authorization
✅ **Testing** - Comprehensive test coverage for models and API endpoints
✅ **Documentation** - Complete API documentation and usage examples

**Tech Stack:** Django 5.2.2 | DRF 3.16.0 | Simple JWT 5.5.0 | Gunicorn | WhiteNoise | Docker

---

Built with ❤️ using Django and Django REST Framework

# 📝 Django Blog Application

- 📄 [View Assignment details](project2/ASSIGNMENT.md)

A simple blog application built using **Django** and **Django REST Framework** that supports CRUD operations, token-based user authentication, and optional frontend integration using either Django templates or React.

---

## 📌 Objective

Build a blog platform where users can:
- Create and manage posts
- Add and view comments
- Use REST APIs for interaction
- Secure actions via token authentication

---

## 🛠️ Features

### ✅ Models
- **Post**
  - `title`: CharField
  - `content`: TextField
  - `author`: ForeignKey (User)
  - `published_date`: DateTimeField

- **Comment**
  - `post`: ForeignKey (to Post)
  - `author`: ForeignKey (User or CharField)
  - `text`: TextField
  - `created_date`: DateTimeField

---

### ✅ APIs (Using DRF)
- **Post API**
  - `GET /api/posts/` – List all posts
  - `POST /api/posts/` – Create a post
  - `GET /api/posts/<id>/` – Retrieve post
  - `PUT /api/posts/<id>/` – Update post
  - `DELETE /api/posts/<id>/` – Delete post

- **Comment API (Nested under Post)**
  - `GET /api/posts/<post_id>/comments/` – List comments
  - `POST /api/posts/<post_id>/comments/` – Create comment

---

### ✅ Authentication
- Uses **Token-based Authentication** via `djangorestframework-simplejwt`
- Endpoints:
  - `POST /api/token/` – Get access and refresh tokens
  - `POST /api/token/refresh/` – Refresh token

Only **authenticated users** can create, update, or delete posts/comments.

---

## 🚀 Optional Frontend

### Django Template Frontend
- Display list of all posts
- View post detail with comments
- Submit new post/comment (authenticated only)

### React Frontend (Optional)
- Integrate using `fetch` or `axios`
- Build components for post list, detail, and comment form

---

## 🧪 Testing

- Basic tests included for:
  - Post and Comment model creation
  - API view access (with and without authentication)
  - Token auth protected routes

Run tests:
```bash
uv run python manage.py test blogapp
```

# 📝 Assignment: Django Blog Application

## 🎯 Objective
Build a simple blog application using **Django** and **Django REST Framework**, integrating basic CRUD (Create, Read, Update, Delete) functionalities.

---

## 📋 Requirements

### 📦 Models

- **Create two models: `Post` and `Comment`.**

#### Post Model
- `title`
- `content`
- `author`
- `published_date`

#### Comment Model
- Linked to the Post model (each post can have multiple comments)
- `author`
- `text`
- `created_date`

---

### 🌐 APIs

- Use **Django REST Framework** to create APIs for the models.

#### Post APIs
- List
- Create
- Retrieve
- Update
- Delete

#### Comment APIs (Under each post)
- List
- Create

---

### 🔗 Views and URLs

- Create corresponding URLs for each API view.
- Ensure that the API returns **JSON** responses.

---

### 🔐 User Authentication

- Implement **token-based authentication**.
- Only **authenticated users** should be able to:
  - Create posts
  - Update posts
  - Delete posts
  - Create comments
  - Delete comments

---

### 🎨 Frontend (Optional)

If you are comfortable with **Django + React**, you can:

- Create a simple frontend to interact with the backend API.
- Implement features such as:
  - Displaying all posts
  - Viewing a single post along with its comments
  - Adding a new post or comment

---

### 📄 Documentation

- Provide a `README.md` file with instructions to set up and run the application.
- Document all API endpoints with request and response examples.

---

### 🧪 Testing

- Write basic tests for:
  - Models
  - API views

---

### ✨ Bonus

- Implement **pagination** for the list of posts.
- Add **"like"** functionality to posts:
  - Users can like a post
  - Display number of likes

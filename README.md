# 📚 Django Book Management System

A web-based **Book Management System** developed using **Django** and **Django REST Framework**.  
This project provides a simple and user-friendly platform to manage books with CRUD operations, search, filtering, authentication, dashboard statistics, and REST API support.

---

## 🚀 Features

- 🔐 User Login and Logout
- 📚 Add Books
- ✏️ Edit Books
- 🗑️ Delete Books
- 🔍 Search Books by Title or Author
- 🏷️ Filter Books by Category
- 📄 Pagination
- 📊 Dashboard with Statistics
- 📈 Category-wise Chart
- 🔌 REST API
- 📥 GET, POST, PUT, PATCH and DELETE API Operations
- 🎨 Bootstrap 5 Responsive UI
- 👤 Login-protected Book Management
- 🛡️ Django Admin Panel
- ✅ Success Messages after CRUD Operations

---

## 🛠️ Technologies Used

- 🐍 Python
- 🌐 Django
- 🔌 Django REST Framework
- 📄 HTML5
- 🎨 CSS3
- 🅱️ Bootstrap 5
- ⚡ JavaScript
- 🗄️ SQLite
- 🔧 Git
- 🐙 GitHub
- 📦 uv

---

## 📂 Project Structure

```text
book/
├── books/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       ├── books/
│       │   ├── dashboard.html
│       │   ├── book_register.html
│       │   └── book_delete.html
│       └── registration/
│           └── login.html
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── screenshots/
│   ├── dashboard.png
│   ├── login.png
│   ├── book-management.png
│   └── api.png
│
├── manage.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
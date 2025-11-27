# AI Dev Tool Zoomcamp

This repository contains my projects and assignments from the **AI Dev Tool Zoomcamp** course.

## 📚 Course Overview

This course covers modern AI-powered development tools and practices, including:
- AI-assisted coding with tools like GitHub Copilot, Cursor, and Claude
- Building web applications with Django
- Testing and deployment best practices
- Working with modern Python tooling (uv, pytest, etc.)

## 🗂️ Repository Structure

```
ai-dev-tool-zoomcamp/
├── 01-todo/          # Django TODO Application
└── README.md         # This file
```

## 📂 Projects

### 01-todo - Django TODO Application

A full-featured TODO application built with Django.

**Features:**
- ✅ Create, read, update, and delete tasks
- ✅ Set due dates for tasks
- ✅ Mark tasks as resolved/unresolved
- ✅ Admin panel for task management
- ✅ Comprehensive test coverage

**Tech Stack:**
- Python 3.12+
- Django 5.2
- SQLite database
- uv for package management

**[View Project →](./01-todo/)**

---

## 🚀 Getting Started

Each project folder contains its own README with specific setup instructions.

### General Prerequisites
- Python 3.12 or higher
- uv (recommended) or pip
- Git

### Quick Start Example (01-todo)

```bash
cd 01-todo
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the app in action.

---

## 📝 License

This repository is for educational purposes as part of the AI Dev Tool Zoomcamp course.

---

## 👤 Author

**Your Name**
- GitHub: [@gilangarito](https://github.com/gilangarito)
- Course: AI Dev Tool Zoomcamp

---

## 🙏 Acknowledgments

- AI Dev Tool Zoomcamp instructors and community
- [DataTalks.Club](https://datatalks.club/) for organizing the course

# Django TODO Application

A simple yet powerful TODO application built with Django as part of the AI Dev Tool Zoomcamp homework.

## ✨ Features

- **Create Tasks**: Add new TODO items with title, description, and due date
- **Edit Tasks**: Update task details and due dates
- **Delete Tasks**: Remove completed or unwanted tasks
- **Mark as Resolved**: Toggle task completion status
- **Admin Panel**: Manage tasks through Django's admin interface

## 🛠️ Tech Stack

- **Framework**: Django 5.2
- **Database**: SQLite3
- **Package Manager**: uv
- **Python**: 3.12+

## 📦 Installation

### Prerequisites
- Python 3.12 or higher
- uv (recommended) or pip

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/gilangarito/ai-dev-tools-course-2025.git
   cd ai-dev-tool-zoomcamp/01-todo
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run migrations**
   ```bash
   uv run python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access)**
   ```bash
   uv run python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   uv run python manage.py runserver
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:8000/`

## 🧪 Running Tests

Run the test suite to verify everything works correctly:

```bash
uv run python manage.py test
```

## 📁 Project Structure

```
django_todo_homework/
├── manage.py
├── todo_project/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todo/                  # Main app
│   ├── models.py         # TodoItem model
│   ├── views.py          # CRUD views
│   ├── urls.py           # URL routing
│   ├── admin.py          # Admin configuration
│   ├── tests.py          # Test cases
│   └── templates/        # HTML templates
│       └── todo/
│           ├── base.html
│           ├── home.html
│           ├── todo_form.html
│           └── todo_confirm_delete.html
└── pyproject.toml        # Dependencies
```

## 🎯 Usage

### Creating a Task
1. Click "Add New Task" button
2. Fill in the title, description (optional), and due date (optional)
3. Click "Save"

### Editing a Task
1. Click "Edit" on any task
2. Modify the fields
3. Click "Save"

### Marking as Resolved
- Click "Mark Resolved" to mark a task as complete
- Click "Mark Unresolved" to revert

### Deleting a Task
1. Click "Delete" on any task
2. Confirm deletion

## 🔑 Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/`

Features:
- View all tasks in a table
- Filter by resolved status and creation date
- Search by title and description
- Bulk actions

## 📝 Date/Time Format

When entering due dates, use one of these formats:
- `YYYY-MM-DD HH:MM:SS` (e.g., `2025-12-25 18:00:00`)
- `YYYY-MM-DD` (e.g., `2025-12-25`)

## 🧩 Models

### TodoItem
- `title` (CharField): Task title
- `description` (TextField): Optional task description
- `due_date` (DateTimeField): Optional due date
- `is_resolved` (BooleanField): Completion status
- `created_at` (DateTimeField): Auto-generated creation timestamp

## 🤝 Contributing

This is a homework project, but suggestions are welcome!

## 📄 License

Educational project for AI Dev Tool Zoomcamp.

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import TodoItem


class TodoItemModelTest(TestCase):
    """Test the TodoItem model"""
    
    def test_create_todo_item(self):
        """Test creating a basic TODO item"""
        todo = TodoItem.objects.create(
            title="Test Task",
            description="Test Description"
        )
        self.assertEqual(todo.title, "Test Task")
        self.assertEqual(todo.description, "Test Description")
        self.assertFalse(todo.is_resolved)
        self.assertIsNotNone(todo.created_at)
    
    def test_todo_item_with_due_date(self):
        """Test creating a TODO with a due date"""
        due_date = timezone.now() + timedelta(days=7)
        todo = TodoItem.objects.create(
            title="Task with deadline",
            due_date=due_date
        )
        self.assertEqual(todo.due_date, due_date)
    
    def test_todo_item_str_method(self):
        """Test the string representation of TodoItem"""
        todo = TodoItem.objects.create(title="My Task")
        self.assertEqual(str(todo), "My Task")


class TodoListViewTest(TestCase):
    """Test the TODO list view"""
    
    def setUp(self):
        self.client = Client()
        # Create some test todos
        TodoItem.objects.create(title="Task 1", description="First task")
        TodoItem.objects.create(title="Task 2", is_resolved=True)
    
    def test_list_view_status_code(self):
        """Test that the list view returns 200"""
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_list_view_template(self):
        """Test that the correct template is used"""
        response = self.client.get(reverse('todo-list'))
        self.assertTemplateUsed(response, 'todo/home.html')
    
    def test_list_view_contains_todos(self):
        """Test that the list view displays todos"""
        response = self.client.get(reverse('todo-list'))
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")


class TodoCreateViewTest(TestCase):
    """Test creating a new TODO"""
    
    def setUp(self):
        self.client = Client()
    
    def test_create_view_status_code(self):
        """Test that the create view returns 200"""
        response = self.client.get(reverse('todo-create'))
        self.assertEqual(response.status_code, 200)
    
    def test_create_todo_post(self):
        """Test creating a TODO via POST"""
        data = {
            'title': 'New Task',
            'description': 'New Description',
        }
        response = self.client.post(reverse('todo-create'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(TodoItem.objects.count(), 1)
        todo = TodoItem.objects.first()
        self.assertEqual(todo.title, 'New Task')


class TodoUpdateViewTest(TestCase):
    """Test updating a TODO"""
    
    def setUp(self):
        self.client = Client()
        self.todo = TodoItem.objects.create(
            title="Original Title",
            description="Original Description"
        )
    
    def test_update_view_status_code(self):
        """Test that the update view returns 200"""
        response = self.client.get(reverse('todo-update', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_update_todo_post(self):
        """Test updating a TODO via POST"""
        data = {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'is_resolved': True
        }
        response = self.client.post(
            reverse('todo-update', args=[self.todo.pk]), 
            data
        )
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Title')
        self.assertTrue(self.todo.is_resolved)


class TodoDeleteViewTest(TestCase):
    """Test deleting a TODO"""
    
    def setUp(self):
        self.client = Client()
        self.todo = TodoItem.objects.create(title="Task to Delete")
    
    def test_delete_view_status_code(self):
        """Test that the delete view returns 200"""
        response = self.client.get(reverse('todo-delete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_todo_post(self):
        """Test deleting a TODO via POST"""
        response = self.client.post(reverse('todo-delete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TodoItem.objects.count(), 0)


class TodoResolveViewTest(TestCase):
    """Test the resolve/unresolve functionality"""
    
    def setUp(self):
        self.client = Client()
        self.todo = TodoItem.objects.create(
            title="Task to Resolve",
            is_resolved=False
        )
    
    def test_resolve_todo(self):
        """Test marking a TODO as resolved"""
        response = self.client.post(reverse('todo-resolve', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_resolved)
    
    def test_unresolve_todo(self):
        """Test marking a resolved TODO as unresolved"""
        self.todo.is_resolved = True
        self.todo.save()
        response = self.client.post(reverse('todo-resolve', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.is_resolved)

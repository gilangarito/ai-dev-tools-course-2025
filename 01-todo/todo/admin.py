from django.contrib import admin
from .models import TodoItem

# Register your models here.
@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'is_resolved', 'created_at']
    list_filter = ['is_resolved', 'created_at']
    search_fields = ['title', 'description']

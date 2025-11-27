from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import TodoItem

class TodoListView(ListView):
    model = TodoItem
    template_name = 'todo/home.html'
    context_object_name = 'todos'
    ordering = ['is_resolved', 'due_date']

class TodoCreateView(CreateView):
    model = TodoItem
    fields = ['title', 'description', 'due_date']
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo-list')

class TodoUpdateView(UpdateView):
    model = TodoItem
    fields = ['title', 'description', 'due_date', 'is_resolved']
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo-list')

class TodoDeleteView(DeleteView):
    model = TodoItem
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo-list')

class TodoResolveView(View):
    def post(self, request, pk):
        todo = get_object_or_404(TodoItem, pk=pk)
        todo.is_resolved = not todo.is_resolved
        todo.save()
        return redirect('todo-list')

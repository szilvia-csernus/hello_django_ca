"""
This module defines the todo views.
"""

from django.shortcuts import render
from .models import Item


def get_todo_list(request):
    """Render Todo List"""
    items = Item.objects.all()

    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

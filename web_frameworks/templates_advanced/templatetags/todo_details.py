from django import template

from templates_advanced.models import Todo

register = template.Library()


@register.inclusion_tag('templates_advanced/tags/todo-item.html')
def todo_details(todo):
    return {
        'todo': todo,
        'todos_count': Todo.objects.count(),
    }

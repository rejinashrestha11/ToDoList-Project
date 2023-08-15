from django.contrib import admin
from .models import Todolist

class TodolistAdmin(admin.ModelAdmin):
    list_display = ('task', 'description', 'due_date', 'completed')

# Register your models here.

admin.site.register(Todolist, TodolistAdmin)
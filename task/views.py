from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView 
from .models import TaskModel

# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
    fields = '__all__'
    model = TaskModel
    context_object_name = 'tasks'
    template_name = 'task/task-list.html'


class TaskDetail(LoginRequiredMixin, DetailView):
    fields = '__all__'
    model = TaskModel
    context_object_name = 'task'
    template_name = 'task/task-detail.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    fields = '__all__'
    model = TaskModel
    success_url = reverse_lazy('tasks')
    template_name = 'task/task-create.html'

class TaskUpdate(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    model = TaskModel
    success_url = reverse_lazy('tasks')
    template_name = 'task/task-update.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = TaskModel
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'task/task-delete.html'

class CustomLogin(LoginView):
    field = '__all__'
    template_name = 'task/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    

from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import TaskDetail, TaskList, TaskCreate, TaskUpdate, TaskDelete, CustomLogin



urlpatterns = [
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<slug:slug>', TaskDetail.as_view(), name='task-detail'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('update-task/<slug:slug>', TaskUpdate.as_view(), name='task-update'),
    path('delete-task/<slug:slug>', TaskDelete.as_view(), name='task-delete'),

]

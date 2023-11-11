from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="todo-home"),
    path('todo/add', views.add, name="todo-add"),
    path('todo/update', views.update, name="todo-update"),
    path('todo/delete/<int:id>', views.delete, name="todo-delete"),
    path('todo/userlist', views.userlist, name="userlist")
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="todo-home"),
    path('todo/add', views.add, name="todo-add"),
    path('todo/update', views.update, name="todo-update"),
    path('todo/delete/<int:id>', views.delete, name="todo-delete"),
    path('todo/userlist', views.userlist, name="userlist"),
    path('user/add/form', views.addUserForm, name="add-user-form"),
    path('user/add', views.addUser, name="add-user"),
    path('user/edit/form/<int:id>', views.editUserForm, name="edit-user-form")
]
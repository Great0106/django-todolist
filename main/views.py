from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    user = request.user

    data = dict(
        todos = Todo.objects.all().order_by("-id").filter(user = user),
        username = user.username,
        user = user
    )
    return render(request, "main/index.html", data)

def add(request):
    user = request.user
    text = request.POST['todo']
    todo = Todo(text=text, user=user).save()

    return HttpResponseRedirect('/')

def update(request):
    if request.POST:
        todo_id = request.POST['todo_id']
        todo = Todo.objects.get(id=todo_id)
        todo.status = not todo.status
        todo.save()

        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return HttpResponseRedirect('/')

def userlist(request):
    user = request.user

    if not user.is_superuser and not user.is_staff:
        return HttpResponseRedirect(reverse('todo-home'))

    all_user = User.objects.all()
    return render(request, 'main/userlist.html', {'users': all_user})

def addUserForm(request):
    return render(request, 'main/add_user_form.html')

def addUser(request):
    if request.POST['password1'] != request.POST['password2']:
        messages.error(request, 'Password does not match!')
        return HttpResponseRedirect(reverse('add-user-form'))

    status = request.POST['status']

    user = User.objects.create_user(
        first_name = request.POST['firstname'],
        last_name = request.POST['lastname'],
        username = request.POST['username'],
        email = request.POST['email'],
        password = request.POST['password1']
    )

    if status == 'admin':
        user.is_staff = True
    elif status == 'superuser':
        user.is_superuser = True
        user.is_staff = True
    
    user.save()
    messages.success(request, 'User added successfully!')
    return HttpResponseRedirect(reverse('userlist'))

def editUserForm(request, id):
    user = User.objects.get(id=id)
    data = dict(
        username = user.username,
        firstname = user.first_name,
        lastname = user.last_name,
        email = user.email,
        is_staff = user.is_staff,
        is_superuser = user.is_superuser,
        is_active = user.is_active
    )
    return render(request, 'main/edit_user_form.html')
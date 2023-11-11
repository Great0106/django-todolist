from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
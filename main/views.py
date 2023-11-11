from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    user = request.user
    all_todos = Todo.objects.all().order_by("-id").filter(user = user)
    return render(request, "main/index.html", {'todos' : all_todos, 'username': user.username})

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
    all_user = User.objects.all()

    return render(request, 'main/userlist.html', {'users': all_user})

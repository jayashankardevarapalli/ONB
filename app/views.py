from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notes, Todo
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


def signin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    noteid = int(request.GET.get('noteid', 0))
    note = Notes.objects.all()

    if request.method == 'POST':
        noteid = int(request.POST.get('noteid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if noteid > 0:
            notes = Notes.objects.get(pk=noteid)
            notes.title = title
            notes.content = content
            notes.save()

            return redirect('/dashboard/?noteid=%i' % noteid)
        else:
            notes = Notes.objects.create(title=title, content=content)

            return redirect('/dashboard/?noteid=%i' % notes.id)

    if noteid > 0:
        notes = Notes.objects.get(pk=noteid)
    else:
        notes = ''

    data = {
        'noteid': noteid,
        'note': note,
        'notes': notes
    }

    return render(request, 'dashboard.html', data)


def todo(request):
    todoid = int(request.GET.get('todoid', 0))
    todos = Todo.objects.all()

    if request.method == 'POST':
        todoid = int(request.POST.get('todoid', 0))
        title = request.POST.get('title')

        if todoid > 0:
            tod = Todo.objects.get(pk=todoid)
            tod.todo = todo
            tod.save()

            return redirect('/todo/?todoid=%i' % todoid)

        else:
            tod = Todo.objects.create(title=title)

            return redirect('/todo/?todoid=%i' % tod.id)

    if todoid > 0:
        tod = Todo.objects.get(pk=todoid)
    else:
        tod = ''

    data = {
        'todoid': todoid,
        'todos': todos,
        'tod': tod
    }

    return render(request, 'todo.html', data)


def delnotes(request, noteid):
    notes = Notes.objects.get(pk=noteid)
    notes.delete()

    return redirect('/dashboard/?noteid=0')


def deltodo(request, todoid):
    tod = Todo.objects.get(pk=todoid)
    tod.delete()

    return redirect('/todo/?todoid=0')


def notes(request):
    note = Notes.objects.all()[:11]

    return render(request, 'notes.html', {'note': note})

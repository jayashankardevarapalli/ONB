from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes,Todo



def index(request):
	return HttpResponse("Index")

def dashboard(request):
	note = Notes.objects.all()[:11]
	todo = Todo.objects.all()[:2]
	data = {
			'note': note,
			'todo': todo
	}
	return render(request, 'dashboard.html', data)

def notes(request):
	note = Notes.objects.all()[:11]
	return render(request, 'notes.html', {'note': note,})

def todo(request):
	todo = Todo.objects.all()[:11]
	return render(request, 'todo.html', {'todo': todo,})

def about(request):
	return render(request, 'about.html')

def create(request):
	return render(request, 'create.html')




from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes,Todo



def index(request):
	return HttpResponse("Index")

def dashboard(request):
	note = Notes.objects.all()[:11]
	todo = Todo.objects.all()[:4]
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

def notescreate(request):
	if request.method == "POST":
		title=request.POST.get('title')
		content=request.POST.get('content')
		notes_data = Notes(title=title, content=content)
		notes_data.save()
		msg = 'Notes saved!! 🗸'
	return render(request, 'dashboard.html', {'msg':msg})




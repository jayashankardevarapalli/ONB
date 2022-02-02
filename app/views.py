from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Notes,Todo



def index(request):
	return HttpResponse("Index")

def about(request):
	return render(request, 'about.html')

def dashboard(request):
	noteid = int(request.GET.get('noteid', 0))
	note = Notes.objects.all()
	todoid = int(request.GET.get('todoid', 0))
	todo = Todo.objects.all()
	

	if request.method == 'POST':
		noteid =  int(request.POST.get('noteid', 0))
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

	if request.method == 'POST':
		todoid = int(request.POST.get('todoid',0))
		title = request.POST.get('todo-title')

		if todoid > 0:
			todos = Todo.objects.get(pk=todoid)
			todos.title = title
			todos.save()

			return redirect('/dashboard/?todoid=%i' % todoid)
		else:
			todos = Todo.objects.create(title=title)

			return redirect('/dashboard/?todoid=%i' %todos.id)

	if todoid > 0:
		todos = Todo.objects.get(pk=todoid)
	else:
		todos = ''



	data = {
			'noteid': noteid,
			'note': note,
			'notes': notes,
			'todoid': todoid,
			'todo': todo,
			'todos': todos
	}

	return render(request, 'dashboard.html', data)

def delnotes(request, noteid):
	notes = Notes.objects.get(pk=noteid)
	notes.delete()

	return redirect('/dashboard/?noteid=0')


def deltodo(request, todoid):
	todos = Todo.objects.get(pk=todoid)
	todos.delete()

	return redirect('/dashboard/?todoid=0')



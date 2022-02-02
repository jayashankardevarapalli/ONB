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
	todo = Todo.objects.all()


	if request.method == 'POST':
		noteid =  int(request.POST.get('noteid', 0))
		title = request.POST.get('title')
		content = request.POST.get('content')

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
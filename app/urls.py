from django.urls import path,include
from .views import index,dashboard,notes,todo,about,notescreate


urlpatterns = [
	path('', index),
	path('dashboard/', dashboard),
	path('notes/', notes),
	path('todo/', todo),
	path('notescreate/', notescreate),
	path('about/', about)
]
from django.urls import path,include
from .views import index,dashboard,notes,todo,about,create


urlpatterns = [
	path('', index),
	path('dashboard/', dashboard),
	path('notes/', notes),
	path('todo/', todo),
	path('create/', create),
	path('about/', about)
]
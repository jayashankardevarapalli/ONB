from django.urls import path,include
from .views import index,dashboard,about,delnotes,notes,todo,deltodo

urlpatterns = [
	path('', index, name='index'),
	path('dashboard/', dashboard, name='dashboard'),
	path('todo/', todo, name='todo'),
	path('delnotes/<int:noteid>', delnotes, name='delnotes'),
	path('deltodo/<int:todoid>', deltodo, name='deltodo'),
	path('notes/', notes, name='notes'),
	path('about/', about, name='about')
]
from django.urls import path,include
from .views import index,dashboard,about,delnotes,notes

urlpatterns = [
	path('', index, name='index'),
	path('dashboard/', dashboard, name='dashboard'),
	path('delnotes/<int:noteid>', delnotes, name='delnotes'),
	path('notes/', notes, name='notes'),
	path('about/', about, name='about')
]
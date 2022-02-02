from django.urls import path,include
from .views import index,dashboard,about,delnotes

urlpatterns = [
	path('', index, name='index'),
	path('dashboard/', dashboard, name='dashboard'),
	path('delnotes/<int:noteid>', delnotes, name='delnotes'),
	path('about/', about, name='about')
]
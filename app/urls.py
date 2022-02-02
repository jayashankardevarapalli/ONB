from django.urls import path,include
from .views import index,dashboard,about

urlpatterns = [
	path('', index, name='index'),
	path('dashboard/', dashboard, name='dashboard'),
	path('about/', about, name='about')
]
from django.urls import path,include
from .views import login,signup


urlpatterns = [
	path('login/', login),
	path('signup/', signup),
]
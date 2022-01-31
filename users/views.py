from django.shortcuts import render
from django.http import HttpResponse


def login(request):
	return HttpResponse("Login")

def signup(request):
	return HttpResponse("SignUp")

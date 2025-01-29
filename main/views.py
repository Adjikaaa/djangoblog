from django.shortcuts import render

def index(request):
	return render(request, "main/index.html")

def about(request):
	return render(request, "main/about.html")

def contact(request):
	return render(request, "main/contact.html")

def service(request):
	return render(request, "main/service.html")
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
	return render(request, "main/index.html")

def about(request):
	return render(request, "main/about.html")

def contact(request):
	return render(request, "main/contact.html")

def postspage(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, "main/postspage.html", {'posts': posts})
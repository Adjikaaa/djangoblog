from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def index(request):
		return render(request, "main/index.html")

def about(request):
		return render(request, "main/about.html")

def contact(request):
		return render(request, "main/contact.html")

def postspage(request):
		posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		return render(request, "main/postspage.html", {'posts': posts})

def post_detail(request, pk):
		post = get_object_or_404(Post, pk=pk)
		return render(request, 'main/post_detail.html', {'post': post})

def create_post(request):
		if request.method == 'POST':
			form = PostForm(request.POST, request.FILES)  # Обратите внимание на request.FILES
			if form.is_valid():
				form.save()
				return redirect('main/postpage')  # Перенаправление после успешного создания
		else:
			form = PostForm()
		return render(request, 'main/create_post.html', {'form': form})


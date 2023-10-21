from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or another appropriate URL
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def article_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'article_details.html', {'post': post})




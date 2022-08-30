from django.shortcuts import render
from . models import Post

# Create your views here.
def bloghome(request):
    posts = Post.objects.all()
    return render(request, 'blog/blogPosts.html', {'posts':posts})

def getpost(request, slug):
    post = Post.objects.get(slug = slug)
    return render(request, 'blog/post.html', {'post': post})
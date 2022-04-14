from django.shortcuts import render
#Models
from .models import Post

# Create your views here.
def posts(request):
    blogs = Post.objects.all()
    return render(request, 'blogs.html')

def post(request, id):
    blog = Post.objects.get(id=id)
    content = f'{blog.title} - {blog.desc}'
    return render(request, 'blog.html')
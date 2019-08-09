from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
def post_list (request):
    posts = Post.objects.all()
    return render(request, 'testapp/post_list.html', {'bala': posts})


def create_post(request):
    pass

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'testapp/post_detail.html', {'post': post})
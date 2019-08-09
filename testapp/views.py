from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list (request):
    posts = Post.objects.all()
    return render(request, 'testapp/post_list.html', {'bala': posts})


def create_post(request):
    pass

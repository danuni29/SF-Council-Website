from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def notice(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'notice/notice_main.html',
        {
            'posts' : posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'notice/single_post_page.html',
        {
            'post': post,
        }


    )

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']
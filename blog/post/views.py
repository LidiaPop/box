from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list_with_bootstrap.html', {'posts': posts})
    # return render(request, 'post_list.html', {'posts': posts})


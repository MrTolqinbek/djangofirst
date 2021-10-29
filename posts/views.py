from django.shortcuts import render, redirect
from .models import Post


def allposts(request):
    posts = Post.objects.all()
    return render(request, "posts/allposts.html", {"posts": posts})


def post(request, pk):
    post = Post.objects.get(id=pk)
    post.views+=1
    post.save()
    return render(request, "posts/post.html", {"post": post})


def like(request, pk):
    print(pk)
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.likes += 1
        post.save()
    return redirect("post",pk =post.id)

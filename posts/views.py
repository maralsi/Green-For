from django.shortcuts import render
from django.http import HttpResponse
import random

from posts.forms import PostForm, PostForm2
from posts.models import Post




# Create your views here.

def green_for(request):
    return HttpResponse(f"Green For {random.randint(0, 1000)}")


def main_view(request):
    if request.method == "GET":
        return render(request, "main.html")


def completed_projects(request):
    if request.method == "GET":
        return render(request, "completed.html")

def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "post_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "post_detail.html")

def post_create(request):
    if request.method == "GET":
        form = PostForm2()
        return render(request, 'post_create.html', context={"form": form})
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "post_create.html", context={"form": form})
        image = form.cleaned_data.get("image")
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        rate = form.cleaned_data.get("rate")
        category = form.cleaned_data.get("category")
        language = form.cleaned_data.get("language")
        # image = request.FILES.get("image")
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # rate = request.POST.get("rate")
        # category = request.POST.get("category")
        # language = request.POST.get("language")
        Post.objects.create(
            image=image,
            title=title,
            content=content,
            rate=rate,
            category=category,
            language=language,

        )
        return HttpResponse("Submitted")






from random import random

from django.contrib.admin.templatetags.admin_list import search_form
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context

from posts.forms import PostForm, PostForm2, SearchForm, PostUpdateForm
from posts.models import Post
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView




class TestView(View):
    def get(self, request):
        return HttpResponse("Hello World")



# Create your views here.

def green_for(request):
    return HttpResponse(f"Green For {random.randint(0, 1000)}")


def main_view(request):
    if request.method == "GET":
        return render(request, "main.html")


def completed_projects(request):
    if request.method == "GET":
        return render(request, "completed.html")


@login_required(login_url='login')
def post_list_view(request):
    if request.method == "GET":
        search = request.GET.get("search")
        tags = request.GET.getlist("tags")
        orderings = request.GET.getlist("ordering")
        searchform = SearchForm(request.GET)
        page = int(request.GET.get("page", 1))
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if tags:
            posts = posts.filter(tags__id__in=tags)
        if orderings:
            posts = posts.order_by(orderings)

        limit = 3
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page * limit
        context = {"posts": posts, "search_form": searchform, "max_pages": range(1, max_pages + 1)}
        return render(request, "post_list.html", context=context)



class PostListView(ListView):
    model = Post
    form = SearchForm()
    template_name = "post_list.html"
    context_object_name = "posts"

@login_required(login_url='login')
def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
    return render(request, "post_detail.html", context=context)

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    lookup_url_kwarg = "post_id"


@login_required(login_url='login')
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
        return redirect("/")

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm2
    template_name = 'post_create.html'
    success_url = '/posts2/'









@login_required(login_url='login')
def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "GET":
        form = PostUpdateForm(instance=post)
        return render(request, "post_update.html", context={"form": form, "post": post})
    if request.method == "POST":
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, "post_update.html", context={"form": form, "post": post})
        form.save()
        return redirect("/profile/")

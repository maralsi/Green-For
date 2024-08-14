from django.shortcuts import render
from django.http import HttpResponse
import random
from posts.models import Post



# Create your views here.

def green_for(request):
    return HttpResponse(f"Green For {random.randint(0, 1000)}")


def main_page(request):
    return render(request, 'main.html')


def completed_projects(request):
    return render(request, 'completed.html')

def post_list_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post_list.html', context)

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})


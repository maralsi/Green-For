"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog import settings
from posts.views import (
    green_for,
    main_view,
    completed_projects,
    post_list_view,
    post_detail_view,
    post_create,
    post_update_view,
    TestView,
    PostListView,
    PostDetailView,
    PostCreateView,


)

from user.views import (
    register_view,
    login_view,
    profile_view
)


from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('green for/', green_for, name='green_for'),
    path('main view/', main_view, name='main'),
    path('completed projects/', completed_projects, name='completed_projects'),
    path('posts/', post_list_view, name="post_list"),
    path('posts/<int:post_id>/', post_detail_view, name='post_detail'),
    path('posts/create/', post_create, name='post_create'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name="login"),
    path('logout/', login_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('post/<int:post_id>/', post_update_view, name='post_update'),
    path('test/', TestView.as_view(), name='test'),
    path('posts2/', PostListView.as_view(), name='post_list2'),
    path('post2/<int:pk>/', PostDetailView.as_view(), name='post_detail2'),
    path('posts2/create/', PostCreateView.as_view(), name='post_create2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.db import models
from pip._vendor.rich.markup import Tag
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True)
    image = models.ImageField(null=True, blank=True, upload_to="posts")
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    field = models.ManyToManyField(Field, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.title

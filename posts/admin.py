
from django.contrib import admin
from posts.models import Post, Category, Field, Language, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'rate', 'category', 'created_at', 'updated_at']
    list_editable = ('rate', 'category')
    list_display_links = ('id', 'title', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at', 'field', 'language', 'field', 'tag')
    search_fields = ('title', 'content', 'field')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


# Register your models here., 'field'

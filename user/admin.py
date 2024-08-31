from django.contrib import admin

from user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_filter = ('user',)
# Register your models here.

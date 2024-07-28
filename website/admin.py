from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
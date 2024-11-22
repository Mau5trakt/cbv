from django.contrib import admin
from books.models import Book

@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


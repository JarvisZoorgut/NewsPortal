from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('postTime', 'title', 'rating', 'author') #не смог добавить категорию
    list_filter = ('postTime', 'rating', 'author')
    search_fields = ('postTime', 'rating', 'author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'ratingAuthor')
    list_filter = ('authorUser', 'ratingAuthor')
    search_fields = ('authorUser', 'ratingAuthor')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentTime', 'comment', 'rating', 'commentUser', 'commentPost') #как сделать по title поста?
    list_filter = ('commentTime', 'comment', 'rating', 'commentUser', 'commentPost')
    search_fields = ('commentTime', 'comment', 'rating', 'commentUser', 'commentPost')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)
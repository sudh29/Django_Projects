from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "get_likes_count")
    list_filter = ("published_date", "author")
    search_fields = ("title", "content")
    readonly_fields = ("published_date",)

    def get_likes_count(self, obj):
        return obj.likes.count()

    get_likes_count.short_description = "Likes"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "author", "post", "created_date")
    list_filter = ("created_date", "author")
    search_fields = ("text", "author__username", "post__title")
    readonly_fields = ("created_date",)

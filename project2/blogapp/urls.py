from django.urls import path
from .views import (
    PostListCreate,
    PostRetrieveUpdateDestroy,
    PostDeleteAll,
    CommentListCreate,
    post_list_view,
    post_detail_view,
)

urlpatterns = [
    path("posts/", PostListCreate.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostRetrieveUpdateDestroy.as_view(), name="post-detail"),
    path(
        "posts/<int:post_pk>/comments/",
        CommentListCreate.as_view(),
        name="comment-list-create",
    ),
    path("posts/delete/", PostDeleteAll.as_view(), name="post-delete-all"),
    path("posts/gui", post_list_view, name="post_list"),
    path("posts/gui/<int:pk>/", post_detail_view, name="post_detail_gui"),
]

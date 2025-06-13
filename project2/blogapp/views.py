"""
APIs:
Utilize Django REST Framework to create APIs for these models.
Implement List, Create, Retrieve, Update, and Delete API views for Post.
Implement List and Create API views for Comment under each Post.
Views and URLs:
Create corresponding URLs for each API view.
Ensure that the API returns JSON responses.
"""

from rest_framework import generics, permissions, response, status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class PostListCreate(generics.ListCreateAPIView):
    """List all posts or create a new post. Only authenticated users can create."""

    queryset = Post.objects.all().order_by("-published_date")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a post by id. Only authenticated users can modify."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentListCreate(generics.ListCreateAPIView):
    """List or create comments for a specific post. Only authenticated users can create."""

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs["post_pk"]
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs["post_pk"]
        serializer.save(author=self.request.user, post_id=post_id)


class PostDeleteAll(generics.DestroyAPIView):
    """Delete all posts. Only admin users can perform this action."""

    queryset = Post.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        deleted_count, _ = Post.objects.all().delete()
        return response.Response(
            {"message": f"{deleted_count} posts deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )


@login_required
def post_list_view(request):
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "blogapp/post_list.html", {"posts": posts})


@login_required
def post_detail_view(request, pk):
    from .models import Post

    post = Post.objects.get(pk=pk)
    return render(request, "blogapp/post_detail.html", {"post": post})

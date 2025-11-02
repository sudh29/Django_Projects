"""
APIs:
Utilize Django REST Framework to create APIs for these models.
Implement List, Create, Retrieve, Update, and Delete API views for Post.
Implement List, Create, and Delete API views for Comment under each Post.
Views and URLs:
Create corresponding URLs for each API view.
Ensure that the API returns JSON responses.
"""

from rest_framework import generics, permissions, response, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone


class PostPagination(PageNumberPagination):
    """Custom pagination for Post list view."""

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only authors to modify their own posts."""

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post
        return obj.author == request.user


class PostListCreate(generics.ListCreateAPIView):
    """List all posts or create a new post. Only authenticated users can create."""

    queryset = Post.objects.all().order_by("-published_date")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a post by id. Only the author can modify."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"
    permission_classes = [IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentListCreate(generics.ListCreateAPIView):
    """List or create comments for a specific post. Only authenticated users can create."""

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs["post_pk"]
        return Comment.objects.filter(post_id=post_id).order_by("-created_date")

    def perform_create(self, serializer):
        post_id = self.kwargs["post_pk"]
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class CommentDestroy(generics.DestroyAPIView):
    """Delete a comment by id. Only authenticated users can delete comments."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs["post_pk"]
        return Comment.objects.filter(post_id=post_id)


class PostLikeToggle(generics.GenericAPIView):
    """Toggle like on a post. Only authenticated users can like posts."""

    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Toggle like status for the current user on the post."""
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True

        return response.Response(
            {"liked": liked, "likes_count": post.likes.count()},
            status=status.HTTP_200_OK,
        )


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
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blogapp/post_detail.html", {"post": post})


def home(request):
    # return HttpResponse("Hello, this is the home page!")
    return render(request, "blogapp/home.html")


class HealthCheckView(APIView):
    """
    Health check endpoint for monitoring and container orchestration
    """

    permission_classes = []

    def get(self, request, *args, **kwargs):
        """
        Return a simple health check response
        """
        # You can add more sophisticated health checks here
        # e.g., database connectivity, cache status, etc.
        return Response(
            {
                "status": "ok",
                "timestamp": timezone.now().isoformat(),
                "service": "django-blog-app",
                "version": "1.0.0",
            }
        )

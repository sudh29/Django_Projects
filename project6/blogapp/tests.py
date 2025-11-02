# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Comment
from rest_framework_simplejwt.tokens import RefreshToken


class PostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="pass")
        self.other_user = User.objects.create_user(username="other", password="pass")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}"
        )
        self.post_url = reverse("post-list-create")
        self.post = Post.objects.create(
            title="Sample", content="Content", author=self.user
        )
        self.detail_url = reverse("post-detail", args=[self.post.pk])

    def test_create_post(self):
        data = {"title": "Hello", "content": "World"}
        response = self.client.post(self.post_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_post(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.post.title)

    def test_update_post(self):
        data = {"title": "Updated", "content": "Updated content"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated")

    def test_delete_post(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_unauthenticated_create(self):
        self.client.credentials()  # Remove auth header
        data = {"title": "NoAuth", "content": "NoAuth"}
        response = self.client.post(self.post_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_update(self):
        self.client.credentials()  # Remove auth header
        data = {"title": "NoAuth", "content": "NoAuth"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_delete(self):
        self.client.credentials()  # Remove auth header
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_author_can_update_own_post(self):
        data = {"title": "Updated by Author", "content": "Updated content"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated by Author")

    def test_other_user_cannot_update_post(self):
        other_refresh = RefreshToken.for_user(self.other_user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {str(other_refresh.access_token)}"
        )
        data = {"title": "Hacked", "content": "Should not work"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_other_user_cannot_delete_post(self):
        other_refresh = RefreshToken.for_user(self.other_user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {str(other_refresh.access_token)}"
        )
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_pagination(self):
        # Create multiple posts
        for i in range(15):
            Post.objects.create(
                title=f"Post {i}", content=f"Content {i}", author=self.user
            )
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertEqual(len(response.data["results"]), 10)  # page_size = 10

    def test_like_post(self):
        like_url = reverse("post-like-toggle", args=[self.post.pk])
        response = self.client.post(like_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["liked"])
        self.assertEqual(response.data["likes_count"], 1)
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())

    def test_unlike_post(self):
        # First like the post
        self.post.likes.add(self.user)
        like_url = reverse("post-like-toggle", args=[self.post.pk])
        # Then unlike it
        response = self.client.post(like_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data["liked"])
        self.assertEqual(response.data["likes_count"], 0)
        self.assertFalse(self.post.likes.filter(id=self.user.id).exists())

    def test_unauthenticated_like_post(self):
        self.client.credentials()  # Remove auth header
        like_url = reverse("post-like-toggle", args=[self.post.pk])
        response = self.client.post(like_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CommentModelTest(APITestCase):
    """Test cases for Comment model."""

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = Post.objects.create(
            title="Test Post", content="Test Content", author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post, author=self.user, text="Test comment"
        )

    def test_comment_str(self):
        self.assertEqual(
            str(self.comment), f"Comment by {self.user.username} on {self.post.title}"
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.text, "Test comment")


class CommentAPITest(APITestCase):
    """Test cases for Comment API endpoints."""

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="pass")
        self.other_user = User.objects.create_user(username="other", password="pass")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}"
        )
        self.post = Post.objects.create(
            title="Test Post", content="Test Content", author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post, author=self.user, text="Test comment"
        )
        self.comment_list_url = reverse("comment-list-create", args=[self.post.pk])
        self.comment_detail_url = reverse(
            "comment-destroy", args=[self.post.pk, self.comment.pk]
        )

    def test_list_comments(self):
        response = self.client.get(self.comment_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_comment(self):
        data = {"text": "New comment"}
        response = self.client.post(self.comment_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(Comment.objects.latest("created_date").text, "New comment")

    def test_unauthenticated_create_comment(self):
        self.client.credentials()  # Remove auth header
        data = {"text": "No auth comment"}
        response = self.client.post(self.comment_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_comment(self):
        response = self.client.delete(self.comment_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())

    def test_unauthenticated_delete_comment(self):
        self.client.credentials()  # Remove auth header
        response = self.client.delete(self.comment_detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_comment_for_nonexistent_post(self):
        invalid_url = reverse("comment-list-create", args=[999])
        data = {"text": "Comment"}
        response = self.client.post(invalid_url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

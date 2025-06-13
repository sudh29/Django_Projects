# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post
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

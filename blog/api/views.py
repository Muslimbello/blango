# from http import HTTPStatus

# from django.urls import reverse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import generics
from blog.api.serializers import PostSerializer
from blog.models import Post

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.fillter(create_time[])
    serializer_class = PostSerializer
# Create your views here.
# def index(request):
#     todo_list = Post.objects.order_by('-create_time')
#     context = {'todo_list': todo_list}
#     return r
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerializer

@api_view(["GET"])
def todolist(req):
    todos = Post.objects.all()
    serializer = PostSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def todocreate(req):
    serializer = PostSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response("POST SUCCESS: " + serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
def tododelete(req, id):
    todos = Post.objects.get(id=id)
    todos.delete()
    return Response("DELETE ID: "+id+" SUCCESS")

@api_view(["PUT"])
def todoupdate(req, id):
    todos = Post.objects.get(id=id)
    serializer = PostSerializer(todos, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response("UPDATE ID: "+id+" SUCCESS")
    return Response(serializer.errors)
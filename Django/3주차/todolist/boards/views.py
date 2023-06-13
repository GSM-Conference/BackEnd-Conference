from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerializer

@api_view(["GET"])
def todolist(req):
    print(req.user)
    todos = Post.objects.filter(author=req.user)
    serializer = PostSerializer(todos, many=True)

    return render(req, 'main.html', {"todos": serializer.data, "user": req.user})

@api_view(["GET"])
def todomake(req):
    return render(req, 'create.html', {'todos': req.data})

@api_view(["GET"])
def todoput(req):
    print(req.query_params)
    return render(req, 'update.html', {'todos': req.query_params.get('id')
})
@api_view(["POST"])
def todocreate(req):
    print(req.data)
    if req.user == 'AnonymousUser':
         print('dong')
    #     return todomake('reject')
    # req.data['author'] = req.user
    serializer = PostSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save(author=req.user)
        return redirect('/board/')
    return Response(serializer.errors)

@api_view(["DELETE"])
def tododelete(req, id):
    todos = Post.objects.get(id=id)
    todos.delete()
    return redirect('/board/')

@api_view(["POST"])
def todoupdate(req, id):
    todos = Post.objects.get(id=id)
    serializer = PostSerializer(todos, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return redirect('/board/')
    return Response(serializer.errors)
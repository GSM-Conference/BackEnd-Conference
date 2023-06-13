from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



@api_view(["GET"])
def signup(req):
    return render(req, 'signup.html', {'todos': req.data})

@api_view(["GET"])
def login(req):
    return render(req, 'login.html', {'todos': req.data})

class SignupView(APIView):
    def post(self, req):
        user = User.objects.create_user(username=req.data['id'], password=req.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return render()

class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['id'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status=401)
        # return Response({"Token": token.key, "User": req.data['id']}, content_type="application/json")
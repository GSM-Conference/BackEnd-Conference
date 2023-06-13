from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class SignupView(APIView):
    def post(self, req):
        user = User.objects.create_user(username=req.data['id'], password=req.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"Token": token.key, "User": req.data['id']}, content_type="application/json")
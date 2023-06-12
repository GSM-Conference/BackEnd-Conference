from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('post', views.PostViewSet)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls))
]
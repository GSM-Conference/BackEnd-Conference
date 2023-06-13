from django.urls import path, include
from .views import SignupView, signup, LoginView
urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('signup_form/', signup),
    path('login/', LoginView.as_view()),
    path('login_form', )
]
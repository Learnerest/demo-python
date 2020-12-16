from django.urls import path
from .views import (
    LikeView,
    register,
    home,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    PostDetailView,
    PostListView,
)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


app_name = "blog_app"
urlpatterns = [
    path("", login_required(PostListView.as_view()), name="blog-home"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/like/<int:pk>", LikeView, name="like_post"),
]

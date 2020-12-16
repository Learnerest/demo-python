from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import RegisterForm, PostForm
from .models import Post
from django.urls import reverse


def LikeView(request, pk):
    likes_connected = get_object_or_404(Post, id=pk)
    if request.method == "POST" and "like" in request.POST:

        likes_connected.likes.add(request.user)
    if request.method == "POST" and "unlike" in request.POST:

        likes_connected.likes.remove(request.user)

    return HttpResponseRedirect(reverse("blog_app:post-detail", args=[str(pk)]))


# Create your views here.
def home(request):

    context = {"objects": Post.objects.all()}
    return render(request, "base.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect("blog_app:login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


class PostListView(ListView):
    model = Post
    template_name = "home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-post_date"]


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    print("hello world")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs["pk"])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data["number_of_likes"] = likes_connected.number_of_likes()
        data["post_is_liked"] = liked
        return data


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "context"]
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "context"]
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/blog"
    template_name = "post_confirm_delete.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

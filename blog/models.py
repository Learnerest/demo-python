from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20, default="Dummy Title")
    context = models.TextField(max_length=150, default="Lorem ipsum...")
    likes = models.ManyToManyField(User, related_name="blogpost_like")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("blog_app:post-detail", kwargs={"pk": self.pk})

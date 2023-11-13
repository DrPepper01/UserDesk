from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField('Categories', related_name='posts_for_cat')

    def __str__(self):
        return self.title


class Categories(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





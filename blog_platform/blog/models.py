from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Profile(AbstractUser):
    # Additional fields for the user profile
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authored_posts')
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_posts')
    
    access_level = models.CharField(max_length=20, choices=(
        ('public', 'Public'),
        ('private', 'Private'),
    ))

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authored_comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

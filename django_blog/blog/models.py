from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager  # If using django-taggit

# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = TaggableManager()  # Tags for categorizing posts

    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title} by {self.author.username}"

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

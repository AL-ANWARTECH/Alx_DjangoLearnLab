from django.contrib import admin
from .models import Post, Profile, Comment  # Import your models

# Register your models
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)

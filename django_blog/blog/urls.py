from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, add_comment, 
    update_comment, delete_comment
)

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Blog Post URLs (CRUD Operations)
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', add_comment, name='add-comment'),  # ✅ Add new comment
    path('comment/<int:pk>/update/', update_comment, name='update-comment'),  # ✅ Update comment
    path('comment/<int:pk>/delete/', delete_comment, name='delete-comment'),  # ✅ Delete comment

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),

    # User Profile Management
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile-update'),
]

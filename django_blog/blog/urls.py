from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Keep for function-based views
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, 
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    PostSearchView, TagDetailView
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

    # Comment URLs (CRUD Operations)
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),

    # User Profile Management
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile-update'),

    # Tag URLs
    path('tag/<str:tag_name>/', TagDetailView.as_view(), name='tag-detail'),

    # Search URLs
    path('search/', PostSearchView.as_view(), name='post-search'),
]

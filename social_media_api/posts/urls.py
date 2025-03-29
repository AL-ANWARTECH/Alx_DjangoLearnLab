from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, PostLikeView, PostUnlikeView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    # Post and Comment URLs
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', 
         CommentViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }), 
         name='post-comments'),
    path('posts/<int:post_pk>/comments/<int:pk>/', 
         CommentViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }), 
         name='comment-detail'),

    # Feed URL
    path('feed/', FeedView.as_view(), name='user-feed'),

    # Like and Unlike Post URLs
    path('posts/<int:pk>/like/', PostLikeView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', PostUnlikeView.as_view(), name='post-unlike'),
]

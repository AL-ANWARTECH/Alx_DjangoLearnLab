from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Post, Like
from accounts.models import User
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    CommentSerializer,
    CommentCreateSerializer
)
from notifications.models import Notification
from .permissions import IsAuthorOrReadOnly

# ViewSet for Posts
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author__username', 'title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PostCreateSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Using generics.get_object_or_404 here
        user = request.user

        # Use get_or_create to avoid multiple likes from the same user
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            return Response(
                {'error': 'You have already liked this post'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a notification if the author is not the same as the liker
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked your post',
                target=post
            )

        return Response({
            'status': 'Post liked',
            'likes_count': post.likes.count()
        })

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Using generics.get_object_or_404 here
        user = request.user

        # Check if the user has liked the post
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response(
                {'error': 'You have not liked this post'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Delete the like
        like.delete()
        return Response({
            'status': 'Post unliked',
            'likes_count': post.likes.count()
        })

# ViewSet for Comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CommentCreateSerializer
        return CommentSerializer

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        if post_pk:
            return self.queryset.filter(post_id=post_pk)
        return self.queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])  # Using generics.get_object_or_404 here
        serializer.save(author=self.request.user, post=post)

# Feed View to Get Posts from Followed Users
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None  # Or use your default pagination

    def get_queryset(self):
        # Get the list of users the current user is following
        following_users = self.request.user.following.all()

        # Get posts from followed users and the current user, ordered by creation date
        posts = Post.objects.filter(
            Q(author__in=following_users) | 
            Q(author=self.request.user)
        ).order_by('-created_at')

        # Optimize database queries
        return posts.select_related('author').prefetch_related('comments', 'likes')
generics.get_object_or_404(Post, pk=pk)
Like.objects.get_or_create(user=request.user, post=post)
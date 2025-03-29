from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import status, viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import CustomUser, Post, Comment
from .serializers import RegisterSerializer, UserSerializer, PostSerializer, CommentSerializer

User = get_user_model()

# Registration view
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login view
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            update_last_login(None, user)
            return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

# Profile view
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Follow user view
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            request.user.following.add(user_to_follow)
            return Response({'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# Unfollow user view
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# User feed view
class UserFeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data)

# Post viewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Comment viewset
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

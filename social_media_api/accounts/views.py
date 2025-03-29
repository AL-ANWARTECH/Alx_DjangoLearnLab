from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer

# User Registration View
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Custom Token View for JWT Authentication
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# User Profile View
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Follow User View
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        if request.user.follow(user_to_follow):
            return Response({'status': f'You are now following {user_to_follow.username}'})
        return Response(
            {'error': 'Unable to follow user'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

# Unfollow User View
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        if request.user.unfollow(user_to_unfollow):
            return Response({'status': f'You have unfollowed {user_to_unfollow.username}'})
        return Response(
            {'error': 'Unable to unfollow user'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

# List of Users Being Followed
class FollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following.all()

# List of Followers
class FollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.followers.all()

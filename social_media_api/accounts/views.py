from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id):
        # Get all users to find the target user
        user_to_follow = get_object_or_404(User.objects.all(), id=user_id)
        
        if request.user.id == user_to_follow.id:
            return Response(
                {'error': 'You cannot follow yourself'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if request.user.following.filter(id=user_to_follow.id).exists():
            return Response(
                {'error': 'You are already following this user'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        request.user.following.add(user_to_follow)
        return Response({
            'status': f'You are now following {user_to_follow.username}',
            'following_count': request.user.following.count()
        })

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id):
        # Get all users to find the target user
        user_to_unfollow = get_object_or_404(User.objects.all(), id=user_id)
        
        if not request.user.following.filter(id=user_to_unfollow.id).exists():
            return Response(
                {'error': 'You are not following this user'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        request.user.following.remove(user_to_unfollow)
        return Response({
            'status': f'You have unfollowed {user_to_unfollow.username}',
            'following_count': request.user.following.count()
        })

class FollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return all users the current user is following
        return self.request.user.following.all()

CustomUser.objects.all() # type: ignore

class FollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return all users following the current user
        return User.objects.filter(following=self.request.user)
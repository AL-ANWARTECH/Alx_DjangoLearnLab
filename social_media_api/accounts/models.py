from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    bio = models.TextField(_('bio'), blank=True)
    profile_picture = models.ImageField(
        _('profile picture'), 
        upload_to='profile_pics/', 
        blank=True, 
        null=True
    )
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True,
        verbose_name=_('following')
    )
    
    def __str__(self):
        return self.username

    def follow(self, user):
        """Follow another user"""
        if user != self and not self.following.filter(id=user.id).exists():
            self.following.add(user)
            return True
        return False

    def unfollow(self, user):
        """Unfollow a user"""
        if user != self and self.following.filter(id=user.id).exists():
            self.following.remove(user)
            return True
        return False

    def is_following(self, user):
        """Check if current user is following the given user"""
        return self.following.filter(id=user.id).exists()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

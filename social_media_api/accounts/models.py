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
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications',
        verbose_name=_('recipient')
    )
    actor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('actor')
    )
    verb = models.CharField(_('verb'), max_length=255)
    read = models.BooleanField(_('read'), default=False)
    timestamp = models.DateTimeField(_('timestamp'), auto_now_add=True)
    
    # Generic foreign key to any related object (dynamic relationships)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['-timestamp']
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')

    def __str__(self):
        return f"{self.actor.username} {self.verb} {self.target}"

    def mark_as_read(self):
        """Marks the notification as read."""
        self.read = True
        self.save()

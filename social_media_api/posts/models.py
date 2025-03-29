from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name=_('author')
    )
    title = models.CharField(_('title'), max_length=255)
    content = models.TextField(
        _('content'),
        blank=True,
        help_text=_('The main content of the post')
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    likes = models.ManyToManyField(
        User,
        related_name='liked_posts',
        blank=True,
        verbose_name=_('likes')
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return f"{self.title} by {self.author.username}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('post')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('author')
    )
    content = models.TextField(
        _('content'),
        help_text=_('The text content of the comment')
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
models.TextField()
from django.contrib.auth import get_user_model
from django.db import models

from posts.constant import MAX_FIELD_LENGTH

User = get_user_model()


class Group(models.Model):
    title = models.CharField(MAX_FIELD_LENGTH)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', null=True, blank=True
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='followers')  # Кто подписан.
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='contentmakers')  # На кого подписан.

    class Meta:
        constraints = [
            # Исключаем дублирование подписок.
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_following'
            ),
            # Запрещаем пользователю подписываться на самого себя.
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='no_self_follow',
            ),
        ]

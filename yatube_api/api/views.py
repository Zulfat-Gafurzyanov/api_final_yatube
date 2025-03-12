# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ReadOnlyModelViewSet

from posts.models import Comment, Group, Post
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)
from .permissions import AuthorOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_post(self):
        # Функция для получения поста.
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        # Формируем queryset.
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        # При создании нового комментария автор автоматически определяется
        # на основе текущего аутентифицированного пользователя.
        serializer.save(author=self.request.user, post=self.get_post())


class ListCreateViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Вьюсет для модели Follow дляобработки двух методов:

    GET — возвращает все подписки пользователя, сделавшего запрос.
    POST — подписать пользователя, сделавшего запрос, на пользователя, 
    переданного в теле запроса.
    """
    pass


class FollowViewSet(ListCreateViewSet):
    """Вьюсет для модели Follow."""
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        # Формируем queryset.
        return self.request.user.followers.all()

    def perform_create(self, serializer):
        # При подписке подписчик автоматически определяется на основе
        # текущего аутентифицированного пользователя.
        serializer.save(user=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """Вьюсет для модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        # При создании нового поста автор автоматически определяется на основе
        # текущего аутентифицированного пользователя.
        serializer.save(author=self.request.user)

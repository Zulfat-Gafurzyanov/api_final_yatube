from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet
)

APIVERSION = 'v1'

router_v1 = SimpleRouter()

router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path(f'{APIVERSION}/', include(router_v1.urls)),
    path(f'{APIVERSION}/', include('djoser.urls.jwt')),
]

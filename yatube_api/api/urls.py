"""Что то слишком просто. Где подвох)?
Может я что то упустил?
"""
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='token-auth'),
]
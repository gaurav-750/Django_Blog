from django.urls import path, include

from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')


# localhost/api/v1/
# urlpatterns = [
#     # path('', PostList.as_view(), name='home'),
#     # path('<int:pk>/', PostDetail.as_view()),

#     # path('users/', UserList.as_view()),
#     # path('users/<int:pk>/', UserDetail.as_view()),
#     # path('', include(router.urls)),

# ]

urlpatterns = router.urls

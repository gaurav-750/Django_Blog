from django.urls import path, include

from .views import PostList, PostDetail, \
    UserViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')


# localhost/api/v1/
urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<int:pk>/', PostDetail.as_view()),

    # path('users/', UserList.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()),
    path('', include(router.urls)),

]

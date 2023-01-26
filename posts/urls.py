from django.urls import path

from .views import PostList, PostDetail

# localhost/api/v1/
urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<int:pk>/', PostDetail.as_view()),
]

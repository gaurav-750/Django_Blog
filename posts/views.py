from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


# *Create your views here.
# class PostList(ListCreateAPIView):
#     # todo Add permission at view level
#     # permission_classes = [IsAuthenticated]

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthorOrReadOnly]

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer


# *Create your views here.
class PostList(ListCreateAPIView):
    # todo Add permission at view level
    # permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

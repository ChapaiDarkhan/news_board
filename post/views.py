from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class NewPostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


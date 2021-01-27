from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer
from .models import Post


class NewPostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

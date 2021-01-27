
from post.views import NewPostView
from django.urls import path

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'new-posts', NewPostView, basename='new-posts')

app_name = "post"
# app_name will help us do a reverse look-up latter.
urlpatterns = router.urls

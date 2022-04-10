from post.views import NewPostView, CommentView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'new-posts', NewPostView, basename='new-posts')
router.register(r'comment', CommentView, basename='comment')

app_name = "post"
# app_name will help us do a reverse look-up latter.
urlpatterns = router.urls

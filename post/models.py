from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=121)
    link = models.URLField()
    votes_number = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField()
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()

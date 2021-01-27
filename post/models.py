from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()


class Post(models.Model):
    created_at = models.DateTimeField()
    description = models.TextField()
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.description


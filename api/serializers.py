from django.db import transaction
from rest_framework import serializers
from post.models import Post, User, Comment


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'name', 'email')


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ('author', 'id', 'title', 'link', 'votes_number', 'created_at', 'description')

    @transaction.atomic
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = User.objects.create(**author_data)
        post = Post.objects.create(author=author, **validated_data)
        return post

    def update(self, instance, validated_data):
        nested_serializer = self.fields['author']
        nested_instance = instance.author
        # note the data is `pop`ed
        nested_data = validated_data.pop('author')
        nested_serializer.update(nested_instance, nested_data)
        # this will not throw an exception,
        # as `profile` is not part of `validated_data`
        return super(PostSerializer, self).update(instance, validated_data)


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('author', 'post', 'id', 'content', 'created_at')

    @transaction.atomic()
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = User.objects.create(**author_data)
        comment = Comment.objects.create(author=author, **validated_data)
        return comment

    def update(self, instance, validated_data):
        nested_serializer = self.fields['author']
        nested_instance = instance.author
        # note the data is `pop`ed
        nested_data = validated_data.pop('author')
        nested_serializer.update(nested_instance, nested_data)
        # this will not throw an exception,
        # as `profile` is not part of `validated_data`
        return super(CommentSerializer, self).update(instance, validated_data)
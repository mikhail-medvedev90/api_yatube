from rest_framework import serializers

from posts.models import Post, Group, Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = 'id', 'title', 'slug', 'description'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Post
        fields = 'id', 'text', 'pub_date', 'author', 'image', 'group'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        read_only_fields = ('post',)
        fields = 'id', 'author', 'post', 'text', 'created'

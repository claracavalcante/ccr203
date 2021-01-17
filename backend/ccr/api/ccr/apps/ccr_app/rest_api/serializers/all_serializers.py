from rest_framework import serializers

from django_blog.apps.account.models import User
from ccr.apps.ccr_app.models import Area, Challenge, Team, Tag, Post, Comment, Meeting


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name',)


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('pk', 'name',)


class ChallengeSerializer(serializers.ModelSerializer):
    areas = AreaSerializer(many=True, required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)
    serializers.FileField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Challenge
        fields = ('pk', 'title', 'description', 'company', 'deadline',
                  'max_number_participants_per_team', 'has_prizes',
                  'image', 'file_description', 'youtube_url', 'areas',)


class TeamSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, required=False, read_only=True)
    challenge = ChallengeSerializer(required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)
    serializers.FileField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Team
        fields = ('pk', 'name', 'description', 'participants', 'image',
                  'solution_file', 'file_url', 'video_url', 'challenge',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk', 'name',)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    author = UserSerializer(required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'body', 'tags', 'author', 'image',)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False, read_only=True)
    post = PostSerializer(required=False, read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'author', 'post', 'up_quantity',)


class MeetingSerializer(serializers.ModelSerializer):
    mentor = UserSerializer(required=False, read_only=True)
    mentee = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'mentor', 'mentee', 'mentor_comments',
                  'mentee_comments', 'deadline',)

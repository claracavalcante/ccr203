from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from ccr.apps.account.models import User
from ccr.apps.ccr_app.models import Area, Challenge, Team, Tag, Post, Comment, Meeting
from ccr.apps.ccr_app.rest_api.serializers.all_serializers import UserSerializer, AreaSerializer, ChallengeSerializer, TeamSerializer, TagSerializer, PostSerializer, CommentSerializer, MeetingSerializer


# User API
class UserListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of users or create new
    """
    serializer_class = UserSerializer
    queryset = User.objects.active()


class UserDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete users
    """
    serializer_class = UserSerializer
    queryset = User.objects.active()


# Challenge API
class ChallengeListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of challenges or create new
    """
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.active()


class ChallengeDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete challenges
    """
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.active()


class ChallengeTeamsAPIView(ListAPIView):
    """
    API view to retrieve list of the teams in a Challenge
    """
    serializer_class = TeamSerializer

    def get_queryset(self):
        challenge_uuid = self.kwargs['pk']
        challenge = Challenge.objects.get(uuid=challenge_uuid)

        return Team.objects.filter(challenge=challenge)


# Team API
class TeamListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of teams or create new
    """
    serializer_class = TeamSerializer
    queryset = Team.objects.active()


class TeamDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete teams
    """
    serializer_class = TeamSerializer
    queryset = Team.objects.active()


# Post API
class PostListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = PostSerializer
    queryset = Post.objects.active()


class PostDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = PostSerializer
    queryset = Post.objects.active()


# CommentSerializer
class CommentListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of comments or create new
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.active()


class CommentDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete comment
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.active()


#  MeetingSerializer
class MeetingListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of meetings or create new
    """
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.active()


class MeetingDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete meeting
    """
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.active()

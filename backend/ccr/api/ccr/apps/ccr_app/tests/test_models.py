from django.test import TestCase

from ccr.apps.ccr_app.models import Challenge, Team, Post, Comment


class ChallengeTestCase(TestCase):
    def test_challenge(self):
        self.assertEquals(
            Challenge.objects.count(),
            0
        )
        Challenge.objects.create(
            title='active', description='description', is_active=True
        )
        Challenge.objects.create(
            title='inactive', description='description', is_active=False
        )
        self.assertEquals(
            Challenge.objects.count(),
            2
        )
        active_challenges = Challenge.objects.active()
        self.assertEquals(
            active_challenges.count(),
            1
        )
        inactive_challenges = Challenge.objects.inactive()
        self.assertEquals(
            inactive_challenges.count(),
            1
        )


class TeamTestCase(TestCase):
    def test_team(self):
        self.assertEquals(
            Team.objects.count(),
            0
        )
        Team.objects.create(name='name')
        self.assertEquals(
            Team.objects.count(),
            1
        )


class PostestCase(TestCase):
    def test_post(self):
        self.assertEquals(
            Post.objects.count(),
            0
        )
        Post.objects.create(title='title', body='body')
        self.assertEquals(
            Post.objects.count(),
            1
        )


class CommentTestCase(TestCase):
    def test_comment(self):
        self.assertEquals(
            Comment.objects.count(),
            0
        )
        Comment.objects.create(text='text')
        self.assertEquals(
            Comment.objects.count(),
            1
        )

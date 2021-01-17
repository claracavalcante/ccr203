from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status

from ccr.apps.ccr_app.models import Challenge, Team, Post, Comment, Area, Tag

# --- Challenge Tests (challenges)


class ChallengeListCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('api-challenge-list', kwargs={'version': 'v1'})

    def test_create_challenge(self):
        self.assertEquals(
            Challenge.objects.count(),
            0
        )
        data = {
            'title': 'title',
            'description': 'description'
        }
        response = self.client.challenge(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Challenge.objects.count(),
            1
        )
        challenge = Challenge.objects.first()
        self.assertEquals(
            challenge.title,
            data['title']
        )
        self.assertEquals(
            challenge.description,
            data['description']
        )

    def test_get_challenge_list(self):
        area = Area(name='area_name')
        area.save()
        challenge = Challenge(title='title1', description='description1')
        challenge.save()
        challenge.areas.add(area)

        response = self.client.get(self.url)
        response_json = response.json()
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            len(response_json),
            1
        )
        data = response_json[0]
        self.assertEquals(
            data['title'],
            challenge.title
        )
        self.assertEquals(
            data['description'],
            challenge.description
        )
        self.assertEquals(
            data['areas'][0]['name'],
            area.name
        )


class ChallengeDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.challenge = Challenge(title='title2', description='description2')
        self.challenge.save()
        self.url = reverse('api-challenge-details',
                           kwargs={'version': 'v1', 'pk': self.challenge.pk})

    def test_get_challenge_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        self.assertEquals(
            data['pk'],
            str(self.challenge.pk)
        )
        self.assertEquals(
            data['title'],
            self.challenge.title
        )
        self.assertEquals(
            data['description'],
            self.challenge.description
        )

    def test_update_challenge(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        data['title'] = 'new_title'
        data['description'] = 'new_description'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.challenge.refresh_from_db()
        self.assertEquals(
            self.challenge.title,
            data['title']
        )
        self.assertEquals(
            self.challenge.description,
            data['description']
        )

    def test_delete_challenge(self):
        self.assertEquals(
            Challenge.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Challenge.objects.count(),
            0
        )


# --- Team Tests (teams) -----------------------------------------------------------------------


class TeamListCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('api-team-list', kwargs={'version': 'v1'})

    def test_create_team(self):
        self.assertEquals(
            Team.objects.count(),
            0
        )
        data = {
            'name': 'name'
        }
        response = self.client.team(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Team.objects.count(),
            1
        )
        team = Team.objects.first()
        self.assertEquals(
            team.name,
            data['name']
        )

    def test_get_team_list(self):
        challenge = Challenge(title='c_title', description="c_description")
        challenge.save()
        team = Team(name='name1', challenge=challenge)
        team.save()

        response = self.client.get(self.url)
        response_json = response.json()
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            len(response_json),
            1
        )
        data = response_json[0]
        self.assertEquals(
            data['name'],
            team.name
        )
        self.assertEquals(
            data['challenges'][0]['title'],
            challenge.title
        )


class TeamDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.team = Team(name='name2')
        self.team.save()
        self.url = reverse('api-team-details',
                           kwargs={'version': 'v1', 'pk': self.team.pk})

    def test_get_team_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        self.assertEquals(
            data['pk'],
            str(self.team.pk)
        )
        self.assertEquals(
            data['name'],
            self.team.name
        )

    def test_update_team(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        data['name'] = 'new_name'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.team.refresh_from_db()
        self.assertEquals(
            self.team.name,
            data['name']
        )

    def test_delete_team(self):
        self.assertEquals(
            Team.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Team.objects.count(),
            0
        )


# --- Post Tests (posts) -----------------------------------------------------------------------


class PostListCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('api-post-list', kwargs={'version': 'v1'})

    def test_create_post(self):
        self.assertEquals(
            Post.objects.count(),
            0
        )
        data = {
            'title': 'title',
            'body': 'body'
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Post.objects.count(),
            1
        )
        post = Post.objects.first()
        self.assertEquals(
            post.title,
            data['title']
        )
        self.assertEquals(
            post.body,
            data['body']
        )

    def test_get_post_list(self):
        tag = Tag(name='tag_name')
        tag.save()
        post = Post(title='title1', body='body1')
        post.save()
        post.tags.add(tag)

        response = self.client.get(self.url)
        response_json = response.json()
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            len(response_json),
            1
        )
        data = response_json[0]
        self.assertEquals(
            data['title'],
            post.title
        )
        self.assertEquals(
            data['body'],
            post.body
        )
        self.assertEquals(
            data['tags'][0]['name'],
            tag.name
        )


class PostDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.post = Post(title='title2', body='body2')
        self.post.save()
        self.url = reverse('api-post-details',
                           kwargs={'version': 'v1', 'pk': self.post.pk})

    def test_get_post_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        self.assertEquals(
            data['pk'],
            str(self.post.pk)
        )
        self.assertEquals(
            data['title'],
            self.post.title
        )
        self.assertEquals(
            data['body'],
            self.post.body
        )

    def test_update_post(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        data['title'] = 'new_title'
        data['body'] = 'new_body'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.post.refresh_from_db()
        self.assertEquals(
            self.post.title,
            data['title']
        )
        self.assertEquals(
            self.post.body,
            data['body']
        )

    def test_delete_post(self):
        self.assertEquals(
            Post.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Post.objects.count(),
            0
        )


# --- Comment Tests (comments) -----------------------------------------------------------------------


class CommentListCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('api-comment-list', kwargs={'version': 'v1'})

    def test_create_comment(self):
        self.assertEquals(
            Comment.objects.count(),
            0
        )
        data = {
            'text': 'text'
        }
        response = self.client.comment(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Comment.objects.count(),
            1
        )
        comment = Comment.objects.first()
        self.assertEquals(
            comment.text,
            data['text']
        )

    def test_get_comment_list(self):
        comment = Comment(text='text1')
        comment.save()

        response = self.client.get(self.url)
        response_json = response.json()
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            len(response_json),
            1
        )
        data = response_json[0]
        self.assertEquals(
            data['text'],
            comment.text
        )

from django.urls import path

from .views import ccr_app_views

urlpatterns = [
    path('users/', ccr_app_views.UserListCreateAPIView.as_view(),
         name='api-user-list'),
    path('users/<uuid:pk>/', ccr_app_views.UserDetailsAPIView.as_view(),
         name='api-user-details'),

    path('challenges/', ccr_app_views.ChallengeListCreateAPIView.as_view(),
         name='api-challenge-list'),
    path('challenges/<uuid:pk>/', ccr_app_views.ChallengeDetailsAPIView.as_view(),
         name='api-challenge-details'),
    path('challenges/<uuid:pk>/teams', ccr_app_views.ChallengeTeamsAPIView.as_view(),
         name='api-challenge-teams'),

    path('teams/', ccr_app_views.TeamListCreateAPIView.as_view(),
         name='api-team-list'),
    path('teams/<uuid:pk>/', ccr_app_views.TeamDetailsAPIView.as_view(),
         name='api-team-details'),

    path('posts/', ccr_app_views.PostListCreateAPIView.as_view(),
         name='api-post-list'),
    path('posts/<uuid:pk>/', ccr_app_views.PostDetailsAPIView.as_view(),
         name='api-post-details'),

    path('meetings/<uuid:pk>/', ccr_app_views.MeetingDetailsAPIView.as_view(),
         name='api-meeting-details'),
]

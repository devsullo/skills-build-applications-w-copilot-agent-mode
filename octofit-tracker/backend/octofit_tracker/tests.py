from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Activity, LeaderboardEntry, Team, User, Workout


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', universe='Test Universe', established=2020)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.universe, 'Test Universe')
        self.assertEqual(self.team.established, 2020)


class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', universe='Test Universe', established=2020)
        self.user = User.objects.create(
            email='test@example.com',
            name='Test User',
            superhero_alias='Test Hero',
            team=self.team
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.superhero_alias, 'Test Hero')
        self.assertEqual(self.user.team, self.team)


class ActivityModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', universe='Test Universe', established=2020)
        self.user = User.objects.create(
            email='test@example.com',
            name='Test User',
            superhero_alias='Test Hero',
            team=self.team
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='Test Activity',
            duration_minutes=30,
            calories=200
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Test Activity')
        self.assertEqual(self.activity.duration_minutes, 30)
        self.assertEqual(self.activity.calories, 200)


class LeaderboardEntryModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', universe='Test Universe', established=2020)
        self.user = User.objects.create(
            email='test@example.com',
            name='Test User',
            superhero_alias='Test Hero',
            team=self.team
        )
        self.entry = LeaderboardEntry.objects.create(user=self.user, score=100, rank=1)

    def test_leaderboard_entry_creation(self):
        self.assertEqual(self.entry.score, 100)
        self.assertEqual(self.entry.rank, 1)


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout',
            difficulty='Easy',
            duration_minutes=20,
            best_for='Everyone'
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.difficulty, 'Easy')


class TeamAPITest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='API Test Team', universe='API Universe', established=2021)

    def test_get_teams(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class UserAPITest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='API Test Team', universe='API Universe', established=2021)
        self.user = User.objects.create(
            email='api@example.com',
            name='API User',
            superhero_alias='API Hero',
            team=self.team
        )

    def test_get_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ActivityAPITest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='API Test Team', universe='API Universe', established=2021)
        self.user = User.objects.create(
            email='api@example.com',
            name='API User',
            superhero_alias='API Hero',
            team=self.team
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='API Activity',
            duration_minutes=45,
            calories=300
        )

    def test_get_activities(self):
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class LeaderboardEntryAPITest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='API Test Team', universe='API Universe', established=2021)
        self.user = User.objects.create(
            email='api@example.com',
            name='API User',
            superhero_alias='API Hero',
            team=self.team
        )
        self.entry = LeaderboardEntry.objects.create(user=self.user, score=150, rank=2)

    def test_get_leaderboard(self):
        url = reverse('leaderboardentry-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class WorkoutAPITest(APITestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='API Workout',
            description='An API test workout',
            difficulty='Medium',
            duration_minutes=30,
            best_for='API Testers'
        )

    def test_get_workouts(self):
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

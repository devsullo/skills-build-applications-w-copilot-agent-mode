from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from pymongo import MongoClient

from octofit_tracker.models import Activity, LeaderboardEntry, Team, User, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting existing test data...')
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel', established=1961)
        dc = Team.objects.create(name='Team DC', universe='DC', established=1934)

        self.stdout.write('Creating superhero users...')
        users = [
            {
                'email': 'tony@stark.com',
                'name': 'Tony Stark',
                'superhero_alias': 'Iron Man',
                'team': marvel,
            },
            {
                'email': 'steve@rogers.com',
                'name': 'Steve Rogers',
                'superhero_alias': 'Captain America',
                'team': marvel,
            },
            {
                'email': 'peter@parker.com',
                'name': 'Peter Parker',
                'superhero_alias': 'Spider-Man',
                'team': marvel,
            },
            {
                'email': 'bruce@wayne.com',
                'name': 'Bruce Wayne',
                'superhero_alias': 'Batman',
                'team': dc,
            },
            {
                'email': 'diana@prince.com',
                'name': 'Diana Prince',
                'superhero_alias': 'Wonder Woman',
                'team': dc,
            },
            {
                'email': 'clark@kent.com',
                'name': 'Clark Kent',
                'superhero_alias': 'Superman',
                'team': dc,
            },
        ]

        user_objs = [User.objects.create(**user_data) for user_data in users]

        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'name': 'Arc Reactor Circuit',
                'description': 'Interval strength training inspired by armor endurance.',
                'difficulty': 'Hard',
                'duration_minutes': 40,
                'best_for': 'Iron Man',
            },
            {
                'name': 'Shield Sprint',
                'description': 'Cardio and agility training for quick recovery.',
                'difficulty': 'Medium',
                'duration_minutes': 30,
                'best_for': 'Captain America',
            },
            {
                'name': 'Web Swing HIIT',
                'description': 'Explosive movement patterns for quick reflexes.',
                'difficulty': 'Medium',
                'duration_minutes': 35,
                'best_for': 'Spider-Man',
            },
            {
                'name': 'Gotham Shadow Training',
                'description': 'Stealth conditioning and endurance drills.',
                'difficulty': 'Hard',
                'duration_minutes': 45,
                'best_for': 'Batman',
            },
            {
                'name': 'Amazon Warrior Flow',
                'description': 'Strength and mobility routines from Themyscira.',
                'difficulty': 'Hard',
                'duration_minutes': 50,
                'best_for': 'Wonder Woman',
            },
            {
                'name': 'Kryptonian Power Cycle',
                'description': 'Explosive power drills optimized for speed.',
                'difficulty': 'Easy',
                'duration_minutes': 25,
                'best_for': 'Superman',
            },
        ]
        Workout.objects.bulk_create([Workout(**workout_data) for workout_data in workouts])

        self.stdout.write('Creating activities...')
        now = timezone.now()
        activities = [
            {
                'user': user_objs[0],
                'activity_type': 'Flight Push',
                'duration_minutes': 50,
                'calories': 650,
                'performed_at': now - timedelta(days=1, hours=2),
            },
            {
                'user': user_objs[1],
                'activity_type': 'Shield Defense',
                'duration_minutes': 35,
                'calories': 420,
                'performed_at': now - timedelta(days=2, hours=3),
            },
            {
                'user': user_objs[2],
                'activity_type': 'Web Sprint',
                'duration_minutes': 30,
                'calories': 380,
                'performed_at': now - timedelta(days=1, hours=5),
            },
            {
                'user': user_objs[3],
                'activity_type': 'Night Patrol',
                'duration_minutes': 60,
                'calories': 720,
                'performed_at': now - timedelta(days=1, hours=1),
            },
            {
                'user': user_objs[4],
                'activity_type': 'Lasso Strength',
                'duration_minutes': 45,
                'calories': 560,
                'performed_at': now - timedelta(days=2, hours=1),
            },
            {
                'user': user_objs[5],
                'activity_type': 'Kryptonian Sprint',
                'duration_minutes': 20,
                'calories': 300,
                'performed_at': now - timedelta(days=1, hours=4),
            },
        ]
        Activity.objects.bulk_create([Activity(**activity_data) for activity_data in activities])

        self.stdout.write('Creating leaderboard entries...')
        leaderboard_entries = [
            {'user': user_objs[2], 'score': 1380, 'rank': 1},
            {'user': user_objs[4], 'score': 1320, 'rank': 2},
            {'user': user_objs[0], 'score': 1290, 'rank': 3},
            {'user': user_objs[1], 'score': 1210, 'rank': 4},
            {'user': user_objs[5], 'score': 1170, 'rank': 5},
            {'user': user_objs[3], 'score': 1130, 'rank': 6},
        ]
        LeaderboardEntry.objects.bulk_create([LeaderboardEntry(**entry_data) for entry_data in leaderboard_entries])

        self.stdout.write('Creating unique index on users.email...')
        client = MongoClient('mongodb://127.0.0.1:27017/')
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Unique index created for users.email'))

        self.stdout.write(self.style.SUCCESS('Database population complete.'))

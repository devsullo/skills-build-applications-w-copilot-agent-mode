from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    universe = models.CharField(max_length=50)
    established = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    superhero_alias = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.superhero_alias} ({self.email})"


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
    performed_at = models.DateTimeField()

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} for {self.user.superhero_alias}"


class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()
    rank = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self):
        return f"#{self.rank} {self.user.superhero_alias}"


class Workout(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration_minutes = models.PositiveIntegerField()
    best_for = models.CharField(max_length=120)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name

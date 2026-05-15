from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, User, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'universe', 'established')
    search_fields = ('name', 'universe')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'superhero_alias', 'team', 'joined_at')
    search_fields = ('email', 'name', 'superhero_alias')
    list_filter = ('team', 'joined_at')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'calories', 'performed_at')
    search_fields = ('activity_type', 'user__superhero_alias')
    list_filter = ('performed_at', 'activity_type')


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'rank', 'last_updated')
    search_fields = ('user__superhero_alias',)
    list_filter = ('rank', 'last_updated')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'duration_minutes', 'best_for')
    search_fields = ('name', 'best_for')
    list_filter = ('difficulty',)

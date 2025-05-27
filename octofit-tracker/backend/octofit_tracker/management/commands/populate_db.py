from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Red Rockets')
        team2 = Team.objects.create(name='Blue Blazers')
        team1.members.set([user1, user2])
        team2.members.set([user3])

        # Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Strength')
        workout2 = Workout.objects.create(name='Running', description='Run 1 mile', suggested_for='Cardio')
        workout3 = Workout.objects.create(name='Plank', description='Hold plank for 1 minute', suggested_for='Core')

        # Activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, points=10)
        Activity.objects.create(user=user2, activity_type='Pushups', duration=10, points=5)
        Activity.objects.create(user=user3, activity_type='Plank', duration=5, points=3)

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=15, month='May')
        Leaderboard.objects.create(team=team2, points=3, month='May')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))

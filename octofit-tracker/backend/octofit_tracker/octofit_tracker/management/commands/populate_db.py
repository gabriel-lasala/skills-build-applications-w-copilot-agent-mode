from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):


        # Always attempt to insert test data, ignore duplicate key errors
        from django.db import IntegrityError

        try:
            marvel = Team.objects.create(name='Marvel', description='Team Marvel')
        except IntegrityError:
            marvel = Team.objects.get(name='Marvel')
        try:
            dc = Team.objects.create(name='DC', description='Team DC')
        except IntegrityError:
            dc = Team.objects.get(name='DC')

        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': marvel},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'team': marvel},
        ]
        dc_heroes = [
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': dc},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc},
        ]
        users = []
        for hero in marvel_heroes + dc_heroes:
            try:
                user = User.objects.create(**hero)
            except IntegrityError:
                user = User.objects.get(email=hero['email'])
            users.append(user)

        try:
            w1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        except IntegrityError:
            w1 = Workout.objects.get(name='Cardio Blast')
        try:
            w2 = Workout.objects.create(name='Strength Training', description='Build muscle and strength')
        except IntegrityError:
            w2 = Workout.objects.get(name='Strength Training')
        w1.suggested_for.add(marvel, dc)
        w2.suggested_for.add(marvel, dc)

        for user in users:
            try:
                Activity.objects.create(user=user, type='Running', duration=30, date=timezone.now().date())
            except IntegrityError:
                pass
            try:
                Activity.objects.create(user=user, type='Cycling', duration=45, date=timezone.now().date())
            except IntegrityError:
                pass

        try:
            Leaderboard.objects.create(team=marvel, points=100)
        except IntegrityError:
            pass
        try:
            Leaderboard.objects.create(team=dc, points=90)
        except IntegrityError:
            pass

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data (or already present).'))

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel')
        dc = Team.objects.create(name='DC', description='Team DC')

        # Create users (superheroes)
        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': marvel},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'team': marvel},
        ]
        dc_heroes = [
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': dc},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc},
        ]
        users = [User.objects.create(**hero) for hero in marvel_heroes + dc_heroes]

        # Create workouts
        w1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        w2 = Workout.objects.create(name='Strength Training', description='Build muscle and strength')
        w1.suggested_for.add(marvel, dc)
        w2.suggested_for.add(marvel, dc)

        # Create activities
        for user in users:
            Activity.objects.create(user=user, type='Running', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, type='Cycling', duration=45, date=timezone.now().date())

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))

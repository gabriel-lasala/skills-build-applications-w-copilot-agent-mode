from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        t = Team.objects.create(name='T', description='d')
        u = User.objects.create(name='U', email='u@x.com', team=t)
        self.assertEqual(str(u), 'U')
    def test_activity_create(self):
        t = Team.objects.create(name='T2', description='d2')
        u = User.objects.create(name='U2', email='u2@x.com', team=t)
        a = Activity.objects.create(user=u, type='Run', duration=10, date='2025-10-24')
        self.assertIn('Run', str(a))
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='d')
        self.assertEqual(str(w), 'W')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='T3', description='d3')
        l = Leaderboard.objects.create(team=t, points=5)
        self.assertIn('Leaderboard', str(l))

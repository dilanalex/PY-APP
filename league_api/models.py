from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ApiTest(models.Model):
    task = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task

##Class Team. a team participates in the league    
class Team(models.Model):
    name = models.TextField(max_length=100)
    abbr = models.TextField(max_length=3)

    def __str__(self):
        return str(self.name)

##Class Game. 
class Game(models.Model):
    QF = 'QF'
    SF = 'SF'
    FI = 'FI'
    WI = 'WI'

    ROUNDS = [
        (QF, 'Quarter Final'),
        (SF, 'Semi Final'),
        (FI, 'Final'),
        (WI, 'Winner')
    ]

    host = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='host')
    guest = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='guest')
    host_score = models.IntegerField()
    guest_score = models.IntegerField()
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winner')
    date = models.DateField(verbose_name='game date')
    round_number = models.CharField(
        max_length=2,
        choices=ROUNDS,
        default=QF,
        verbose_name='round type'
    )

    def __str__(self):
        return 'Game # %s' % (self.id)



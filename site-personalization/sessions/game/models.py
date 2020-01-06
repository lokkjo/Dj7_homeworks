from random import randint

from django.db import models


class Player(models.Model):
    participating_the_game = models
    is_gamemaster = models.BooleanField()



class Game(models.Model):
    target_number = models.IntegerField(default=randint(0, 10))
    is_resolved = models.BooleanField(default=False)


class PlayerGameInfo(models.Model):
    pass

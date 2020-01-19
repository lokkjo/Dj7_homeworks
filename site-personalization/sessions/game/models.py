from random import randint

from django.db import models


class Player(models.Model):
    participating_the_game = models.ManyToManyField(
        'Game', through='PlayerGameInfo', related_name='games'
        )
    is_gamemaster = models.BooleanField()



class Game(models.Model):
    target_number = models.IntegerField(default=randint(0, 10))
    is_resolved = models.BooleanField(default=False)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


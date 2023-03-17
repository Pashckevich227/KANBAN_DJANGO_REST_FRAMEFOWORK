import datetime

from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):
    YELLOW = 'yellow'
    GREEN = 'green'
    RED = 'red'
    LIGHT_BLUE = 'light-blue'
    BLUE = 'blue'
    PURPLE = 'purple'
    VIOLET = 'violet'
    ORANGE = 'orange'

    COLOR_CHOICES = [
        (YELLOW, 'yellow'),
        (GREEN, 'green'),
        (RED, 'red'),
        (LIGHT_BLUE, 'light-blue'),
        (BLUE, 'blue'),
        (PURPLE, 'purple'),
        (VIOLET, 'violet'),
        (ORANGE, 'orange'),
    ]

    name = models.CharField(max_length=50)
    color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default=RED,
    )
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mark(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    priority = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=datetime.datetime.now())
    deadline = models.DateTimeField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name





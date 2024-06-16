from django.db import models

class Lead(models.Model):
    HOT = 'hot'
    COLD = 'cold'
    BOMB = 'bomb'
    VOM = 'vom'

    CHOICE_STATUS = [
        (HOT, 'Hot'),
        (COLD, 'Cold'),
        (BOMB, 'Bomb'),
        (VOM, 'VOM'),
    ]

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=4, choices=CHOICE_STATUS, default=HOT)

    def __str__(self):
        return self.name

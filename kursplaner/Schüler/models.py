from django.db import models

# Create your models here.
class Schueler(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    alter = models.IntegerField(
        blank=True,
        null=True
    )

    class Skilllevel(models.TextChoices):
        LEVEL_0 = '0',
        LEVEL_1 = '1',
        LEVEL_2 = '2',
        LEVEL_3 = '3',
        LEVEL_4 = '4',
        LEVEL_5 = '5',
        LEVEL_6 = '6',
        LEVEL_7 = '7',

    Skillevel_Ski=models.CharField(
        max_length=2,
        choices=Skilllevel.choices,
        default=Skilllevel.LEVEL_0,
    )
    Skillevel_Snowboard = models.CharField(
        max_length=2,
        choices=Skilllevel.choices,
        default=Skilllevel.LEVEL_0,
    )
    Skillevel_Langlauf = models.CharField(
        max_length=2,
        choices=Skilllevel.choices,
        default=Skilllevel.LEVEL_0,
    )
    Skillevel_Telemark = models.CharField(
        max_length=2,
        choices=Skilllevel.choices,
        default=Skilllevel.LEVEL_0,
    )
    telefonnummer = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
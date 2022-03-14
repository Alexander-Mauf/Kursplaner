from django.db import models
from Lehrer.models import Lehrer
from Schüler.models import Schueler
from django.dispatch import receiver

# Create your models here.
class Kurs(models.Model):

    class Kurstypen(models.TextChoices):
        SKI_GRUPPE = 'SG', ('Ski Gruppe')
        SKI_PRIVAT = 'SP', ('Ski Privat')
        SNOWBOARD_GRUPPE = 'SBG', ('Snowboard Gruppe')
        SNOWBOARD_PRIVAT = 'SBP', ('Snowboard Privat')
        LANGLAUF_PRIVAT = 'LL', ('Langlauf')
        TELEMARK_PRIVAT = 'TM', ('Telemark')


    class Timeslot(models.TextChoices):
        NINE_TO_TEN = "09:00", ("09:00 - 10:00")
        TEN_TO_TWELVE = "10:00", ("10:00 - 12:00")
        TWELVE_TO_ONE = "12:00", ("12:00 - 13:00")
        AFTERNOON = "13:30", ("13:30 - 15:30")

    class Skilllevel(models.TextChoices):
        LEVEL_0 = '0',"Beginner"
        LEVEL_1 = '1',
        LEVEL_2 = '2',
        LEVEL_3 = '3',
        LEVEL_4 = '4',
        LEVEL_5 = '5',
        LEVEL_6 = '6',
        LEVEL_7 = '7',

    kurs_typ = models.CharField(
        max_length=3,
        choices=Kurstypen.choices,
        null=False,
    )

    skill_level = models.CharField(
        max_length=2,
        choices=Skilllevel.choices,
        default=Skilllevel.LEVEL_0,
    )

    time = models.CharField(
        max_length=5,
        choices=Timeslot.choices,

    )
    lehrer = models.ForeignKey(
        Lehrer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    datum = models.DateField(
        blank=False,
    )

    # hier sollen dann die schüler verknüpft werden
    teilnehmer = models.ManyToManyField(
        Schueler
    )
    #lehrer = models.ManyToManyField()
    #
    #


    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=("Erstellt am:")
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Geändert am:")
    )
    def __str__(self):
        return f"{str(self.kurs_typ)}-{str(self.time)}-{str(self.skill_level)}-{str(self.lehrer)}"
    def __repr__(self):
        return self.name

@receiver(models.signals.post_save, sender=Kurs)
def statechange_post_save(sender, instance, created, **kwargs):
    if created:
        pass
    # wenn kein Lehrer gesetzt ist -> einen aussuchen
    # check availability for Lehrer
    # check work-prio
    # check knowledge width -> first use up ppl who can do only 1 thing



class Tagesplan(models.Model):
    lehrer = models.ForeignKey(Lehrer,on_delete=models.CASCADE)
    day = models.DateField()
    nine_to_ten = models.ForeignKey(Kurs, related_name="9-10+", on_delete=models.CASCADE, null=True, blank=True)
    ten_to_twelve = models.ForeignKey(Kurs, related_name="10-12+", on_delete=models.CASCADE, null=True, blank=True)
    twelve_to_one = models.ForeignKey(Kurs, related_name="12-13+", on_delete=models.CASCADE, null=True, blank=True)
    thirteen_thirty_to_fifteen_thirty = models.ForeignKey(Kurs, related_name="13:30-15:30+", on_delete=models.CASCADE, null=True, blank=True)



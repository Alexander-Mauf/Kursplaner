from django.db import models

from django.dispatch import receiver

class Skillevel:
    BEGINNER = 'Beginner'
    LEVEL_1 = 'Level 1'
    LEVEL_2 = 'Level 2'
    LEVEL_3 = 'Level 3'
    LEVEL_4 = 'Level 4'
    LEVEL_5 = 'Level 5'
    LEVEL_6 = 'Level 6'
    LEVEL_7 = 'Level 7'


class Skills(models.Model):
    ski_alpin = models.CharField(
        max_length=255,
        choices=(
            (Skillevel.BEGINNER, Skillevel.BEGINNER),
            (Skillevel.LEVEL_1, Skillevel.LEVEL_1),
            (Skillevel.LEVEL_2, Skillevel.LEVEL_2),
            (Skillevel.LEVEL_3, Skillevel.LEVEL_3),
            (Skillevel.LEVEL_4, Skillevel.LEVEL_4),
            (Skillevel.LEVEL_5, Skillevel.LEVEL_5),
            (Skillevel.LEVEL_6, Skillevel.LEVEL_6),
            (Skillevel.LEVEL_7, Skillevel.LEVEL_7),
        ),
        default=Skillevel.BEGINNER
    )
    snowboard = models.CharField(
        max_length=255,
        choices=(
            (Skillevel.BEGINNER, Skillevel.BEGINNER),
            (Skillevel.LEVEL_1, Skillevel.LEVEL_1),
            (Skillevel.LEVEL_2, Skillevel.LEVEL_2),
            (Skillevel.LEVEL_3, Skillevel.LEVEL_3),
            (Skillevel.LEVEL_4, Skillevel.LEVEL_4),
            (Skillevel.LEVEL_5, Skillevel.LEVEL_5),
            (Skillevel.LEVEL_6, Skillevel.LEVEL_6),
            (Skillevel.LEVEL_7, Skillevel.LEVEL_7),
        ),
        default=Skillevel.BEGINNER
    )
    ski_cross_country = models.CharField(
        max_length=255,
        choices=(
            (Skillevel.BEGINNER, Skillevel.BEGINNER),
            (Skillevel.LEVEL_1, Skillevel.LEVEL_1),
            (Skillevel.LEVEL_2, Skillevel.LEVEL_2),
            (Skillevel.LEVEL_3, Skillevel.LEVEL_3),
            (Skillevel.LEVEL_4, Skillevel.LEVEL_4),
            (Skillevel.LEVEL_5, Skillevel.LEVEL_5),
            (Skillevel.LEVEL_6, Skillevel.LEVEL_6),
            (Skillevel.LEVEL_7, Skillevel.LEVEL_7),
        ),
        default=Skillevel.BEGINNER
    )
    ski_tele = models.CharField(
        max_length=255,
        choices=(
            (Skillevel.BEGINNER, Skillevel.BEGINNER),
            (Skillevel.LEVEL_1, Skillevel.LEVEL_1),
            (Skillevel.LEVEL_2, Skillevel.LEVEL_2),
            (Skillevel.LEVEL_3, Skillevel.LEVEL_3),
            (Skillevel.LEVEL_4, Skillevel.LEVEL_4),
            (Skillevel.LEVEL_5, Skillevel.LEVEL_5),
            (Skillevel.LEVEL_6, Skillevel.LEVEL_6),
            (Skillevel.LEVEL_7, Skillevel.LEVEL_7),
        ),
        default=Skillevel.BEGINNER
    )


class Customer(Skills, models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Vorname',
        null=True,
        blank=True
    )
    surname = models.CharField(
        max_length=255,
        verbose_name='Nachname',
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Teacher(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Vorname'
    )
    surname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Nachname'
    )
    has_licence = models.BooleanField(
        default=False
    )
    can_ski_alpin = models.BooleanField(
        default=False
    )
    can_snowboard = models.BooleanField(
        default=False
    )
    can_ski_cross_country = models.BooleanField(
        default=False
    )
    can_ski_telemark = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Seasons:
    SEASON_21_22 = '21/22'
    SEASON_22_23 = '22/23'
    SEASON_23_24 = '23/24'
    SEASON_24_25 = '24/25'


class ClassTimes:
    PRIVAT_MORNING = '09:00-10:00'
    GROUP_MORNING = '10:00-12:00'
    PRIVAT_NOON = '12:00-13:00'
    GROUP_AFTERNOON = '13:30-15:30'
    PRIVAT_AFTERNOON = '15:30-16:30'
    SONDER = 'Außerplanmäßig'


class Timeslot(models.Model):
    date = models.DateField()
    slot = models.CharField(
        max_length=255,
        choices=(
            (ClassTimes.PRIVAT_MORNING, ClassTimes.PRIVAT_MORNING),
            (ClassTimes.GROUP_MORNING, ClassTimes.GROUP_MORNING),
            (ClassTimes.PRIVAT_NOON, ClassTimes.PRIVAT_NOON),
            (ClassTimes.GROUP_AFTERNOON, ClassTimes.GROUP_AFTERNOON),
            (ClassTimes.PRIVAT_AFTERNOON, ClassTimes.PRIVAT_AFTERNOON),
            (ClassTimes.SONDER, ClassTimes.SONDER),
        ),
        default=ClassTimes.GROUP_MORNING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.date} {self.slot}'

    def __str__(self):
        return f'{self.date} {self.slot}'

    class Meta:
        unique_together = ('date', 'slot')
        indexes = [models.Index(fields=['date']), ]


class Sportarten:
    SKI_ALPIN = 'ski-alpin'
    SKI_CROSS_COUNTRY = 'langlauf'
    SKI_TELE = 'telemark'
    SNOWBOARD = 'snowboard'


class Class(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    timeslot = models.ForeignKey(
        Timeslot,
        on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=255,
        choices=(
            (Sportarten.SKI_ALPIN, Sportarten.SKI_ALPIN),
            (Sportarten.SNOWBOARD, Sportarten.SNOWBOARD),
            (Sportarten.SKI_CROSS_COUNTRY, Sportarten.SKI_CROSS_COUNTRY),
            (Sportarten.SKI_TELE, Sportarten.SKI_TELE),
        )
    )
    students = models.ManyToManyField(
        Customer,
        blank=True,
        related_name="students"
    )
    private = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.timeslot} {self.type} {self.teacher}'

    def __str__(self):
        return f'{self.timeslot} {self.type} {self.teacher}'


class AvailabilityStatus:
    AVAILABLE = 'verfügbar'
    NOT_AVAILABLE = 'nicht verfügbar'
    ONLY_EMERGENCIES = 'nur Notfälle'
    UNCLEAR = 'unklar'


class Availability(models.Model):
    slot = models.ForeignKey(
        Timeslot,
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    availability = models.CharField(
        max_length=255,
        choices=(
            (AvailabilityStatus.AVAILABLE, AvailabilityStatus.AVAILABLE),
            (AvailabilityStatus.NOT_AVAILABLE, AvailabilityStatus.NOT_AVAILABLE),
            (AvailabilityStatus.ONLY_EMERGENCIES, AvailabilityStatus.ONLY_EMERGENCIES),
            (AvailabilityStatus.UNCLEAR, AvailabilityStatus.UNCLEAR)
        ),
        default=AvailabilityStatus.NOT_AVAILABLE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.teacher} {self.slot} {self.availability}'

    def __str__(self):
        return f'{self.teacher} {self.slot} {self.availability}'


    class Meta:
        indexes = [
            models.Index(fields=['teacher']),
        ]




@receiver(models.signals.post_save, sender=Class)
def credential_post_save(sender, instance, created, **kwargs):
    if created:
        # block Lehrer availability for the timeslot
        teacher_availability = models.Availability.objects.filter(teacher=instance.teacher, slot=instance.timeslot).first()
        teacher_availability.availability = AvailabilityStatus.NOT_AVAILABLE # @todo dies muss zu hat Kurs refactored werden

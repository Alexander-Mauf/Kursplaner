from django.db import models

# Create your models here.
class Lehrer(models.Model):
    name = models.CharField(
        max_length=255,
    )

    class AusbildungsLevel(models.TextChoices):
        KEINE_KENTNISSE = '0', ('Keine Kentnisse')
        INTERN_ANGELERNT = '1', ('Ausbildungswochenende mitgemacht')
        DSV_GRUNDSTUFE = '2', ('DSV Grundstufe/DSLV Level 2')
        DSV_INSTRUCTOR = '3', ('DSV Instructor/DSLV Level 3')
        DSV_SKILEHRER = '4', ('DSV Skilehrer/Staatlich geprüfter Skilehrer')

    ski_level = models.CharField(
        max_length=2,
        choices=AusbildungsLevel.choices,
        default=AusbildungsLevel.KEINE_KENTNISSE,
    )

    snowboard_level = models.CharField(
        max_length=2,
        choices=AusbildungsLevel.choices,
        default=AusbildungsLevel.KEINE_KENTNISSE,
    )

    telemark_level = models.CharField(
        max_length=2,
        choices=AusbildungsLevel.choices,
        default=AusbildungsLevel.KEINE_KENTNISSE,
    )

    langlauf_level = models.CharField(
        max_length=2,
        choices=AusbildungsLevel.choices,
        default=AusbildungsLevel.KEINE_KENTNISSE,
    )

    # dies soll ein array der Tage werden an denen der Lehrer arbeiten kannn
    verfuegbarkeit = [models.DateField(
    )]


    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=("Erstellt am:")
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Geändert am:")
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name



import django_tables2 as tables
from . import models

class CustomerTable(tables.Table):
    name = tables.Column(
        accessor='name',
        verbose_name='Vorname',
        orderable=False,
        attrs={
            "td": {
                "class": "column-wrap",
            }
        }
    )
    surname = tables.Column(
        accessor='surname',
        verbose_name='Nachname',
        orderable=False,
        attrs={
            "td": {
                "class": "column-wrap",
            }
        }
    )
    class Meta:
        model = models.Customer
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "surname", "address")

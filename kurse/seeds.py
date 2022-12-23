import datetime
import logging
from . import models


def seed_all_timeslots_for_day(**kwargs) -> None:
    day = kwargs.get('day')
    if day is None:
        day = datetime.date.today()
    slots = [x for x in models.ClassTimes.__dict__ if not x.startswith('__')]

    for x in slots:
        slot, _ = models.Timeslot.objects.get_or_create(
            slot=x,
            date=day
        )
    logging.info(f'alle Slots für Tag {day} geseedet')
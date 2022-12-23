from django.core.management.base import BaseCommand
import datetime

from django.core.management.base import BaseCommand
from kurse import models


class Command(BaseCommand):
    help = 'Seeds all the timeslots for all defined seasons.'

    def add_arguments(self, parser):
        parser.add_argument('mandant', nargs='?', type=str, default=['pointpro-secrets-prod', ])

    def handle(self, *args, **options):
        seasons = [x for x in models.Seasons.__dict__ if not x.startswith('__')]

        for season in seasons:
            # find all dates in a season
            parts = season.split('_')
            first_year = parts[1]
            second_year = parts[2]
            # y-m.d
            date_1 = datetime.date(int(f'20{first_year}'), 12, 10)
            date_2 = datetime.date(int(f'20{second_year}'), 4, 15)
            # create all timeslots
            delta = date_2 - date_1
            for i in range(delta.days + 1):
                day = date_1 + datetime.timedelta(days=i)
                from kurse import seeds
                seeds.seed_all_timeslots_for_day(day=day)

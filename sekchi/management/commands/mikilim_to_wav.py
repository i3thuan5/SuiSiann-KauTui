from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from pathlib import Path
import sys
import re


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=1, type=str)

    def handle(self, *args, **options):
        path = options['path'][0]
        nikiliman = []
        for file in Path(path).glob('**/*'):
            matched = re.match(r'[Pp]art([0-9])-\(([0-9]{1,4})\)\.wav', file.name)
            if not matched:
                print(file.name)
                continue
            part, number = matched.group(1, 2)
            nikiliman.append((file, part, number))

        for i in sorted(
                nikiliman,
                key=lambda element: (element[1], int(element[2]))
            ):
            print(i)

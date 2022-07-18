from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.files import File
from django.db import transaction
from sekchi.models import Sekchi
from pathlib import Path
import re


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        path = settings.SIKTSI_ROOT
        nikiliman = []
        for file in Path(path).glob('**/*.wav'):
            tongmia = file.name
            matched = re.match(r'[Pp]art([0-9])-\(([0-9]{1,4})\)\.wav', tongmia)
            if matched:
                part, number = matched.group(1, 2)
                nikiliman.append((file, part, number))
            elif tongmia == '洪錦田.wav':
                nikiliman.append((file, '1', '190'))
            elif tongmia == 'part1-(1951)-1.wav':
                nikiliman.append((file, '1', '1951'))
            elif tongmia == '2869-1(phian).wav':
                nikiliman.append((file, '3', '2869'))
            else:
                print(file.name)
                continue

        for 音檔檔名, part, 編號 in sorted(
            nikiliman,
            key=lambda element: (element[1], int(element[2]))
        ):
            Sekchi.objects.create(音檔所在=音檔檔名, part=part, 編號=編號)

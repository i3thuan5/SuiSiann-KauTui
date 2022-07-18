from django.core.management.base import BaseCommand
from django.core.files import File
from django.db import transaction
from sekchi.models import Sekchi
from pathlib import Path
import re


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', default='/汐止媠聲', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        path = options['path']
        nikiliman = []
        for file in Path(path).glob('**/*'):
            matched = re.match(r'[Pp]art([0-9])-\(([0-9]{1,4})\)\.wav', file.name)
            if not matched:
                print(file.name)
                continue
            part, number = matched.group(1, 2)
            nikiliman.append((file, part, number))

        for 音檔, part, 編號 in sorted(
                    nikiliman,
                    key=lambda element: (element[1], int(element[2]))
                ):
            with open(音檔, mode='rb') as f:
                myfile = File(f)
                Sekchi.objects.create(音檔=myfile, part=part, 編號=編號)

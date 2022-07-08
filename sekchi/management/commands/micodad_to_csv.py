from django.core.management.base import BaseCommand
from sekchi.models import Sekchi
from pathlib import Path
import csv

def micodad(path):
    with open(path, mode='r') as f:
        reader = csv.DictReader(f)

        part_dict = {}
        for row in reader:
            part_dict[row['編號']] = row['漢字']
        return part_dict

class Command(BaseCommand):

    def handle(self, *args, **options):
        which_part = {
            str(n): micodad(f'sekchi/csv/part{n}.csv') for n in range(1, 5)
        }

        for i in Sekchi.objects.all():
            i.漢字 = which_part[i.part][i.編號]
            i.save()

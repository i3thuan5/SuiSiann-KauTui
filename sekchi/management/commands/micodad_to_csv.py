from django.core.management.base import BaseCommand
from django.db import transaction
from sekchi.models import Sekchi
import csv


def micodad(path):
    with open(path, mode='r') as f:
        reader = csv.DictReader(f)
        ayaw = None
        part_dict = {}
        for row in reader:
            if row['來源'] == '':
                row['來源'] = ayaw
            part_dict[row['編號']] = (row['漢字'], row['來源'])
            ayaw = row['來源']
        return part_dict


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
        which_part = {}
        for n in range(1, 5):
            which_part[str(n)] = micodad(f'sekchi/csv/part{n}.csv')
        for i in Sekchi.objects.filter(漢字=''):
            i.漢字 = which_part[i.part][i.編號][0]
            i.來源 = which_part[i.part][i.編號][1]
            i.save()

from django.core.management.base import BaseCommand
from sekchi.models import Sekchi
from pathlib import Path
import csv

def micodad():
    with open('sekchi/csv/part1.csv', mode='r') as f:
        reader = csv.DictReader(f)

        part1_dict = {}
        for row in reader:
            part1_dict[row['編號']] = row['漢字']
        print(part1_dict)

class Command(BaseCommand):

    def handle(self, *args, **options):
        micodad()

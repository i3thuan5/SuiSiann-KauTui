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
        part1_dict = micodad('sekchi/csv/part1.csv')
        part2_dict = micodad('sekchi/csv/part2.csv')
        part3_dict = micodad('sekchi/csv/part3.csv')
        part4_dict = micodad('sekchi/csv/part4.csv')

        which_part = {
            '1': part1_dict,
            '2': part2_dict,
            '3': part3_dict,
            '4': part4_dict,
        }

        for i in Sekchi.objects.all():
            print(i.part, i.編號)
            i.漢字 = which_part[i.part][i.編號]
            print(i.漢字)
            i.save()

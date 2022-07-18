from django.core.management.base import BaseCommand
from kupan.models import Lē as Le, Khuán as Khuan
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('kupan/教育部文章.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                khuan, _ = Khuan.objects.get_or_create(miâ=row['篇名'])
                le = Le.objects.get(id=row['語料庫ID'])
                # print(khuan, le)
                le.tó一款句辦.add(khuan)

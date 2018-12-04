from django.core.management.base import BaseCommand
import argparse
from sunko.models import 句表
from django.db import transaction


class Command(BaseCommand):
    help = '逐篇文章音檔kah句的csv檔，寄入來db'
    
    def add_arguments(self, parser):
        parser.add_argument('--csv', nargs='+', type=argparse.FileType('r'))
        
    def handle(self, *args, **options):    
        for csvTong in options['csv']:
            for tsua in csvTong:
                print(tsua)
    
    @classmethod
    def csv寄入去db(cls, 一筆):
        一句物件 = 句表(
            音檔=一筆['Im-tóng'],
            漢字=一筆['Hàn-jī'],
            臺羅=一筆['Lô-má-jī']
        )
        一句物件.save()
        
    
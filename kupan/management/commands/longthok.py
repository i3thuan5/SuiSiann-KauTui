from django.core.management.base import BaseCommand
from kupan.models import Lē as Le, Khuán as Khuan


ID_PIAUTE = [
    (10066, 10097, '豆花'),
    (10098, 10131, '四秀仔'),
    (10132, 10165, '寫大字'),
    (10166, 10202, '捌校園'),
    (10203, 10239, '鼓勵'),
    (10240, 10276, '土檨仔'),
    (10277, 10308, '工課'),
    (10309, 10343, '洗身軀'),
    (10344, 10374, '烏豆乾'),
    (10375, 10403, '𨑨迌物'),
    (10404, 10438, '阿媽'),
    (10439, 10470, '縛粽'),
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        for thau, boe, piaute in ID_PIAUTE:
            khuan, _ = Khuan.objects.get_or_create(miâ=piaute)
            for le in Le.objects.filter(id__gte=thau, id__lte=boe):
                le.tó一款句辦.add(khuan)

# Generated by Django 3.2.5 on 2021-08-30 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Khuán',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miâ', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Khuán',
                'verbose_name_plural': 'Khuán',
            },
        ),
        migrations.CreateModel(
            name='Tsònghóng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miâ', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Tsònghóng',
                'verbose_name_plural': 'Tsònghóng',
            },
        ),
        migrations.CreateModel(
            name='Lē',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('音檔', models.FileField(blank=True, upload_to='')),
                ('漢字', models.TextField()),
                ('羅馬字含口語調', models.TextField()),
                ('羅馬字', models.TextField(editable=False)),
                ('修改時間', models.DateTimeField(auto_now=True)),
                ('對齊狀態', models.CharField(blank=True, default='-', max_length=200)),
                ('備註', models.TextField(blank=True)),
                ('tó一款句辦', models.ManyToManyField(blank=True, to='kupan.Khuán')),
                ('修改人', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('校對狀況', models.ManyToManyField(blank=True, to='kupan.Tsònghóng')),
            ],
            options={
                'verbose_name': 'Lē',
                'verbose_name_plural': 'Lē',
            },
        ),
    ]

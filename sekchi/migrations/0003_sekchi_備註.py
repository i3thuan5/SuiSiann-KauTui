# Generated by Django 4.0.6 on 2022-07-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekchi', '0002_sekchi_來源_alter_sekchi_part_alter_sekchi_編號'),
    ]

    operations = [
        migrations.AddField(
            model_name='sekchi',
            name='備註',
            field=models.TextField(blank=True),
        ),
    ]

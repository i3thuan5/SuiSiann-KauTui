# Generated by Django 4.0.6 on 2022-07-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekchi', '0003_sekchi_備註'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tsònghóng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miâ', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Tsònghóng',
                'verbose_name_plural': 'Tsònghóng',
            },
        ),
        migrations.AddField(
            model_name='sekchi',
            name='校對狀況',
            field=models.ManyToManyField(blank=True, to='sekchi.tsònghóng'),
        ),
    ]

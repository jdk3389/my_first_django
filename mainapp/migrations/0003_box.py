# Generated by Django 4.0.4 on 2022-06-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_ship_created_date_remove_ship_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipId', models.FloatField(default=0)),
                ('width', models.FloatField()),
                ('depth', models.FloatField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('underWaterVolume', models.FloatField()),
                ('globalShipPosition', models.TextField()),
                ('shipAttitude', models.TextField()),
                ('localCOG', models.TextField()),
                ('globalCOG', models.TextField()),
                ('localCOB', models.TextField()),
                ('globalCOB', models.TextField()),
                ('draft', models.FloatField()),
                ('heel', models.FloatField()),
                ('trim', models.FloatField()),
            ],
        ),
    ]

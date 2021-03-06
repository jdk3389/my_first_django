# Generated by Django 4.0.4 on 2022-06-08 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('shipId', models.IntegerField(default=0, primary_key=True, serialize=False)),
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
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

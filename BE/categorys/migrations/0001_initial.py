# Generated by Django 3.2.12 on 2022-08-11 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dong',
            fields=[
                ('dong_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sido_name', models.CharField(max_length=20)),
                ('gugun_name', models.CharField(max_length=20)),
                ('dong_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gugun',
            fields=[
                ('gugun_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gugun_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('job_main_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('job_main_category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sido',
            fields=[
                ('sido_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sido_name', models.CharField(max_length=20)),
            ],
        ),
    ]

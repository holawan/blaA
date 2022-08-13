# Generated by Django 3.2.12 on 2022-08-13 04:51

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
            name='Crew',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('crew_pk', models.AutoField(primary_key=True, serialize=False)),
                ('is_business', models.BooleanField()),
                ('crew_name', models.CharField(max_length=50, unique=True)),
                ('crew_img', models.ImageField(blank=True, default='crew/image/상점기본.png', null=True, upload_to='crew/image')),
                ('crew_explain', models.TextField()),
                ('crew_region', models.TextField(blank=True, null=True)),
                ('crew_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('crew_member', models.ManyToManyField(blank=True, related_name='crews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CrewArticle',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('crew_article_pk', models.AutoField(primary_key=True, serialize=False)),
                ('crew_title', models.CharField(max_length=50)),
                ('crew_content', models.TextField()),
                ('crew_private', models.BooleanField(default=False)),
                ('crew_pin', models.BooleanField(default=False)),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.crew')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CrewSchedule',
            fields=[
                ('crew_schedule_pk', models.AutoField(primary_key=True, serialize=False)),
                ('crew_day', models.DateField()),
                ('color', models.CharField(max_length=20)),
                ('crew_starthour', models.TimeField()),
                ('crew_endhour', models.TimeField()),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.crew')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CrewInvite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew_leader_accept', models.BooleanField()),
                ('user_accept', models.BooleanField()),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.crew')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CrewChat',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chat_pk', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.crew')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CrewArticleImage',
            fields=[
                ('article_image_pk', models.AutoField(primary_key=True, serialize=False)),
                ('article_picture', models.ImageField(upload_to='crew_article/image')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.crewarticle')),
            ],
        ),
        migrations.CreateModel(
            name='CrewArticleComment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('crew_comment_pk', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.crewarticle')),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.crew')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]

# Generated by Django 3.2.12 on 2022-08-16 02:29

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
            name='Story',
            fields=[
                ('story_pk', models.AutoField(primary_key=True, serialize=False)),
                ('story_title', models.CharField(max_length=50)),
                ('story_picture', models.ImageField(upload_to='user/story/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('region', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('like_user', models.ManyToManyField(related_name='like_story', to=settings.AUTH_USER_MODEL)),
                ('user_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('hashtag_pk', models.AutoField(primary_key=True, serialize=False)),
                ('hashtag_content', models.CharField(max_length=20)),
                ('story_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.story')),
                ('user_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_pk', models.AutoField(primary_key=True, serialize=False)),
                ('story_comment', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('story_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.story')),
                ('user_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

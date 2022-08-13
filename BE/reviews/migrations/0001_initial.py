# Generated by Django 3.2.12 on 2022-08-13 09:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review_pk', models.AutoField(primary_key=True, serialize=False)),
                ('star', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('oneline_review', models.TextField(null=True)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_pk', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, default='store/logo/상점기본.png', null=True, upload_to='store/logo')),
                ('region', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreButtonReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.buttonreview')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.review')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.store')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='reviews.store'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-17 11:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blogs', '0003_alter_blog_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='Blog_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]

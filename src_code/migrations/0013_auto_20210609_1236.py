# Generated by Django 2.2.17 on 2021-06-09 12:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('src_code', '0012_detail_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to=settings.AUTH_USER_MODEL),
        ),
    ]
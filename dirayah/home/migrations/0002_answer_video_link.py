# Generated by Django 4.1.3 on 2022-12-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='video_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-08-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leetcode', '0002_leetcode_change_leetcode_contests_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leetcode',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
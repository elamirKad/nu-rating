# Generated by Django 4.1 on 2022-08-16 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leetcode', '0004_contest_contestuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestuser',
            name='contest',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='leetcode.contest'),
        ),
    ]

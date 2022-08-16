# Generated by Django 4.1 on 2022-08-16 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leetcode', '0003_leetcode_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPorblems', models.IntegerField()),
                ('title', models.CharField(max_length=1000)),
                ('starttime', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ContestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.BooleanField(default=False)),
                ('trend', models.CharField(default='NONE', max_length=1000)),
                ('solved', models.IntegerField(default=0)),
                ('finish', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=1500)),
                ('ranking', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leetcode.leetcode')),
            ],
        ),
    ]
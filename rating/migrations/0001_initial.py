# Generated by Django 4.1 on 2022-08-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('overall', models.FloatField()),
                ('easy', models.FloatField()),
                ('knowledge', models.FloatField()),
                ('fun', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('professors', models.ManyToManyField(to='rating.professor')),
            ],
        ),
    ]

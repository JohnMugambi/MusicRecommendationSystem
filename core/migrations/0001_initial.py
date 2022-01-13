# Generated by Django 3.2.7 on 2022-01-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListeningHistory',
            fields=[
                ('index', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('number_0', models.TextField(blank=True, db_column='0', null=True)),
            ],
            options={
                'db_table': 'listening_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PopularSongs',
            fields=[
                ('index', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('user_id', models.TextField(blank=True, null=True)),
                ('song', models.TextField(blank=True, null=True)),
                ('score', models.BigIntegerField(blank=True, null=True)),
                ('rank', models.FloatField(blank=True, db_column='Rank', null=True)),
            ],
            options={
                'db_table': 'popular_songs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecommendedSongs',
            fields=[
                ('index', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('user_id', models.TextField(blank=True, null=True)),
                ('song', models.TextField(blank=True, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('rank', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'recommended_songs',
                'managed': False,
            },
        ),
    ]
# Generated by Django 3.2.7 on 2022-01-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongData',
            fields=[
                ('song_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('release', models.TextField()),
                ('artist_name', models.TextField()),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'tblsongslibrary',
                'managed': False,
            },
        ),
    ]
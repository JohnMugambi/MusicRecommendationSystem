from django.db import models


# Create your models here.

class ListeningHistory(models.Model):
    index = models.BigIntegerField(blank=True,  primary_key=True)
    number_0 = models.TextField(db_column='0', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'listening_history'


class PopularSongs(models.Model):
    index = models.BigIntegerField(blank=True,  primary_key=True)
    user_id = models.TextField(blank=True, null=True)
    song = models.TextField(blank=True, null=True)
    score = models.BigIntegerField(blank=True, null=True)
    rank = models.FloatField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'popular_songs'


class RecommendedSongs(models.Model):
    index = models.BigIntegerField(blank=True,  primary_key=True)
    user_id = models.TextField(blank=True, null=True)
    song = models.TextField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    rank = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommended_songs'


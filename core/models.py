from django.db import models
from django.contrib.auth.models import User

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


class SongData(models.Model):
    song_id = models.CharField(primary_key=True, max_length=100)
    title = models.TextField()
    release = models.TextField()
    artist_name = models.TextField()
    year = models.IntegerField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblsongslibrary'


class Tbllisteninghistory(models.Model):
    song_listened_id = models.AutoField(primary_key=True)
    user_id = models.TextField()
    song_id = models.TextField()
    listen_count = models.IntegerField()
    title = models.TextField()
    release = models.TextField()
    artist_name = models.TextField()
    year = models.TextField()  # This field type is a guess.
    song = models.TextField()

    class Meta:
        managed = False
        db_table = 'tbllisteninghistory'


class Tblsongslibrary(models.Model):
    song_id = models.CharField(primary_key=True, max_length=100)
    title = models.TextField()
    release = models.TextField()
    artist_name = models.TextField()
    year = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblsongslibrary'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

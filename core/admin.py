from django.contrib import admin
from .models import RecommendedSongs, SongData, PopularSongs, ListeningHistory, Tblsongslibrary, Tbllisteninghistory


# Register your models here.
admin.site.register(RecommendedSongs)
admin.site.register(SongData)
admin.site.register(PopularSongs)
admin.site.register(ListeningHistory)
admin.site.register(Tblsongslibrary)
admin.site.register(Tbllisteninghistory)



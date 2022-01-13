from django.shortcuts import render
import pandas as pd
from .models import RecommendedSongs, PopularSongs, ListeningHistory
from .main_engine import popularityengine, recommendedsongsengine, searchsimilarsong
from .mldata import content


def home(request):
    popularityengine()
    popular_songs = PopularSongs.objects.all()
    return render(request, "core/index.html", {'popular_songs': popular_songs})


def search(request):
    #print(dir(request)) # print(request.GET)
    query_dict = dict(request.GET)
    query = query_dict.get('search_song')
    similar_songs_list = ''
    if query is not None:
        song_object = searchsimilarsong(query)
        similar_songs_list = song_object['song']
        similar_songs_list = similar_songs_list.to_list()
    return render(request, "core/search.html", {'similar_songs': similar_songs_list},)


def profile(request):
    recommendedsongsengine()
    recommended_songs = RecommendedSongs.objects.all()
    listening_history = ListeningHistory.objects.all()
    return render(request, "core/profile.html", {'recommended_songs': recommended_songs, 'listening_history': listening_history})

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import RecommendedSongs, PopularSongs, ListeningHistory, SongData
from .main_engine import popularityengine, recommendedsongsengine, searchsimilarsong
from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('/')
    else:
        form = UserRegistrationForm()

    return render(request, "core/register.html", {'form': form})


def home(request):
    popularityengine()
    popular_songs = PopularSongs.objects.all()
    return render(request, "core/index.html", {'popular_songs': popular_songs})


@login_required()
def search(request):
    #print(dir(request)) # print(request.GET)
    query_dict = dict(request.GET)
    query = query_dict.get('search_song')
    similar_songs_list = ''
    songs_by_year = SongData.objects.order_by('-year')[:10]
    list_of_songs = SongData.objects.order_by()
    if query is not None:
        song_object = searchsimilarsong(query)
        similar_songs_list = song_object['song']
        similar_songs_list = similar_songs_list.to_list()

    return render(request, "core/search.html", {'similar_songs': similar_songs_list, 'discover_songs': songs_by_year},)


@login_required()
def profile(request):
    current_user = request.user
    current_user = current_user.username
    recommendedsongsengine(current_user)
    recommended_songs = RecommendedSongs.objects.all()
    listening_history = ListeningHistory.objects.all()
    return render(request, "core/profile.html", {'recommended_songs': recommended_songs,
                                                 'listening_history': listening_history})

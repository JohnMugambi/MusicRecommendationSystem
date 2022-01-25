from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import RecommendedSongs, PopularSongs, ListeningHistory, SongData
from .main_engine import popularityengine, recommendedsongsengine, searchsimilarsong
from .forms import UserRegistrationForm, UserUpdateForm, ProfileImageUpdateForm
from background_task import background

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
    if request.user.is_authenticated:
        current_user = request.user
        current_user = current_user.username
        recommendedsongsengine(current_user)

        print("User is authenticated")
        return render(request, "core/index.html", {'popular_songs': popular_songs})
    else:
        print("User is not authenticated")
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
    recommended_songs = RecommendedSongs.objects.all()
    listening_history = ListeningHistory.objects.all()
    return render(request, "core/profile.html", {'recommended_songs': recommended_songs,
                                                 'listening_history': listening_history})


def update_profile(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        #image_form = ProfileImageUpdateForm(request.POST, request.FILES, instance=request.user.username)
        if update_form.is_valid():
            update_form.save()
            #image_form.save()
            messages.success(request, f'Your profile information has been updated!')
            # Redirect to profile page
            return redirect('profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
        #image_form = ProfileImageUpdateForm(instance=request.user.username)
    context = {
        'u_form': update_form
    }
    return render(request, "core/update_profile.html", context)

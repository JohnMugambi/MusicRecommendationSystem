from . import Recommenders
import pandas as pd
from sqlalchemy import create_engine
import os
from django.conf import settings


###Database Connection
engine = create_engine("mysql+mysqlconnector://root:mugambi@localhost/recommender_db", echo=True)


#Loading datasets 'data/triplets_file.csv'
song_df_1 = pd.read_csv(os.path.join(settings.DATA_FILES, 'triplets_file.csv'))
song_df_2 = pd.read_csv(os.path.join(settings.DATA_FILES, 'song_data.csv'))
#Combine both data
song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on='song_id', how='left')

###Data preprocessing
# creating new feature combining title and artist name
song_df['song'] = song_df['title'] + '-' + song_df['artist_name']
#Taking top 10k samples
song_df = song_df.head(1000)

###Cummulative sum of listen counts of the songs
song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage'] = song_grouped['listen_count'] / grouped_sum * 100
song_grouped.sort_values(['listen_count', 'song'], ascending=[0, 1])


def popularityengine():
    ###Popularity recommendation engine
    pr = Recommenders.popularity_recommender_py()
    pr.create(song_df, 'user_id', 'song')
    ###display the top 10 popular songs
    top_ten_songs = pr.recommend(song_df['user_id'][1])
    # top 10 songs based on popularity
    top_ten_songs.to_sql(con=engine, name="popular_songs", if_exists='replace', index=True)


def recommendedsongsengine(logged_in_user_id):
    ###Get users index
    logged_user = song_df[song_df['user_id'] == logged_in_user_id]
    logged_user_index = logged_user.tail(1).index.item()
    ###Item Similarity recommendation engine
    ir = Recommenders.item_similarity_recommender_py()
    ir.create(song_df, 'user_id', 'song')
    user_items = ir.get_user_items(song_df['user_id'][logged_user_index])
    user_items_df = pd.DataFrame(user_items)

    #Display user songs history
    #for user_item in user_items:
    #    print(user_item)

    ###Give song recommendation for that user
    ir1 = ir.recommend(song_df['user_id'][logged_user_index])

    #print(ir1.head())
    # user-listening history
    user_items_df.to_sql(con=engine, name="listening_history", if_exists='replace', index=True)

    # recommended songs based on users history
    ir1.to_sql(con=engine, name="recommended_songs", if_exists='replace', index=True)


def searchsimilarsong(song_name):
    ir = Recommenders.item_similarity_recommender_py()
    ir.create(song_df, 'user_id', 'song')
    # give related songs based on the words
    results = ir.get_similar_items(song_name)
    return results




# import
import pandas as pd
import matplotlib.pyplot as plt 
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas



# extract data
spotify_data = pd.read_csv('spotify_songs.csv')

#cleaning missing values
spotify_data["track_name"].fillna("Unknown_track", inplace=True)
spotify_data["track_artist"].fillna("Unknown_artist", inplace=True)
spotify_data["track_album_name"].fillna("Unknown_album", inplace=True)


# transfter data
spotify_data['track_album_release_date'] = pd.to_datetime(spotify_data['track_album_release_date'], errors='coerce', format='%Y-%m-%d')



# load data
conn = snowflake.connector.connect(
user="HAITHM",
password="Haitham12",
account="KAOFXXH-JT03374",
database="PYTHON",
schema="PYTHON"
)

write_pandas(conn , spotify_data , "Spotify" ,auto_create_table=True)












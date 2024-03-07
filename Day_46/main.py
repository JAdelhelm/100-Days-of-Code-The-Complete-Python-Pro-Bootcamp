#%%
import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint

# INPUT = input("Which year do want to travel to? Type the date in the first format YYYY-MM-DD")



import spotipy
from spotipy.oauth2 import SpotifyOAuth
 
CLIENT_ID_SPOTIFY = ""
CLIENT_SECRET_SPOTIFY = ""
URL_REDIRECT = "http://example.com"
 
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID_SPOTIFY,
        client_secret=CLIENT_SECRET_SPOTIFY,
        show_dialog=True,
        cache_path="token.txt",
        # username=YOUR SPOTIFY DISPLAY NAME, 
    )
)
# access_token = sp.get_access_token()

user_id = sp.current_user()["id"]

# INPUT = "2014-02-13"
date = input("Which year do want to travel to? Type the date in the first format YYYY-MM-DD")

URL_WEBSITE = f"https://www.billboard.com/charts/hot-100/{date}/"

pprint(URL_WEBSITE)

response = requests.get(URL_WEBSITE)
content = response.text

soup = BeautifulSoup(content, "lxml")

title_music_elements = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in title_music_elements]

pprint(song_names)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
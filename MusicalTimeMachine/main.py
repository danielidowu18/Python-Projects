import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "840554921b5744bb9d163883006ac082"
CLIENT_SECRET = "7ed6333d972d479db0a3bda38c8fd8e9"
REDIRECT_URL = "http://example.com"
SCOPE = "playlist-modify-private"

date = input("What year you would like to travel to in YYYY-MM-DD format? ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"


with requests.get(url=URL) as response:
    contents = response.text

soup = BeautifulSoup(contents, "html.parser")
songs = []
for item in soup.find_all(attrs={"class":"o-chart-results-list-row-container"}):
    song = item.h3.get_text(strip=True)
    songs.append(song)


client = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL, scope=SCOPE)
client.get_access_token()

user = spotipy.client.Spotify(oauth_manager=client)
user_detail = user.current_user()
USER_ID = user_detail["id"]


track_ids = []
for song in songs:
    track = user.search(q=song, type="track")
    try:
        track_id = track["tracks"]["items"][0]["id"]
        track_ids.append(track_id)
    except:
        pass


playlist_details = user.user_playlist_create(user=USER_ID, name=f"{date} Billboard 100", public=False)
playlist_id = playlist_details["id"]


for track in track_ids:
    user.user_playlist_add_tracks(user=USER_ID, playlist_id=playlist_id, tracks=[track])


playlist = user.playlist(playlist_id=playlist_id)
print(playlist)

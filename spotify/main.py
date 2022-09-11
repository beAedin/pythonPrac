from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

URL = "https://www.billboard.com/charts/hot-100/"
redirect = 'http://example.com'
api_id = os.environ.get("spotify_id")
api_pw = os.environ.get("spotify_pw")

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

res = requests.get(URL+year+"/")

web = res.text

soup = BeautifulSoup(web, "html.parser")

music_list = soup.find_all(name="h3", id="title-of-a-story")

musics = [music.getText().strip("\t\n") for music in music_list]
print(musics)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",  redirect_uri=None,
client_id=api_id, client_secret=api_pw, show_dialog=True, cache_path="token.txt"))

user_id = sp.current_user()["id"]
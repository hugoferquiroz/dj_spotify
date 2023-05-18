import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics.pairwise import linear_model
# import numpy as np

class SpotipyClient():
    
    # Métodos
    def __init__(self):
        scope = 'user-top-read,user-library-read'
        # Atributos
        client_id = '923e41f1eb3f4f638b102398bb2bee6b'      # Your client id
        client_secret = 'fc0ad2c973de49b99ce16d84e86f0f14'  # Your secret
        redirect_uri = 'http://127.0.0.1:5000/api_callback' # Your uri callback

        # Client credentials
        client_credentials_manager = SpotifyOAuth(client_id=client_id, 
                                                  client_secret=client_secret,
                                                  scope=scope)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                                  requests_timeout=30)
        me = self.sp.me()
        username = me['id']
        print(username)
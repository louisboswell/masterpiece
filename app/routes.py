from flask import render_template
from flask_sqlalchemy import model
from app import app, db

import spotipy
from spotipy.oauth2 import SpotifyOAuth

@app.route('/')
def index():
    
    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_saved_tracks()
    
    return render_template('index.html', results=results)
from flask import render_template
from flask_sqlalchemy import model
from app import app, db

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

@app.route('/')
def index():
    
    results = []
    
    playlists = sp.user_playlists('spotify')
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
            results.append(playlist['name'])
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    
    return render_template('index.html', results=results)

@app.route('/search/<name>')
def search(name):
    
    results = sp.search(q=str(name), type="album", limit=10)
    
    temp = []

    for i, album in enumerate(results['albums']['items']):
    
        x = {
            "name": album['name'],
             "artist": album['artists'][0]['name']
            }
        
        temp.append(x)
    
    return render_template('search.html', results=temp)

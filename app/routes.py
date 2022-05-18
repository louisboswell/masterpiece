from flask import render_template, url_for, redirect
from flask_sqlalchemy import model
from app import app, db
from app.forms import SearchForm

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/search/<name>', methods=['POST', 'GET'])
def search(name):
    form = SearchForm()
    
    if form.validate_on_submit():
        return redirect(url_for('search', name=form.query.data))
    
    results = sp.search(q=str(name), type="album", limit=10)
    
    temp = []

    for i, album in enumerate(results['albums']['items']):
    
        x = {
            "name": album['name'],
            "artist": album['artists'][0]['name'],
            "url": album['images'][0]['url']
            }

        temp.append(x)
    
    return render_template('search.html', results=temp, form=form)

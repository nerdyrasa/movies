import json
import os

from flask import render_template

from ..models import Movie
from . import main


@main.route('/')
def index():
    # read datafile
    datafile = os.path.join(os.getcwd(), 'data', 'movie_list.json')
    with open(datafile) as movie_file:
        movie_data = json.load(movie_file)

    # iterate through the movie_data and create instance of Movie object
    movie_list = [Movie(movie) for movie in movie_data]

    return render_template('index.html', movie_list=movie_list)

import fresh_tomatoes
import json
import media

# open json file 
with open("movie_list.json") as movie_file:
    movie_data = json.load(movie_file)

movie_list = []

# iterate through the movie_data and create instance of Movie object
for movie in movie_data:
    movie_list.append(media.Movie(movie))

# create the html page    
fresh_tomatoes.open_movies_page(movie_list)



import sys
import fresh_tomatoes
import json
import media


def main():
    """Main entry point for app"""
    # open json file
    with open("movie_list.json") as movie_file:
        movie_data = json.load(movie_file)

    # iterate through the movie_data and create instance of Movie object
    movie_list = [media.Movie(movie) for movie in movie_data]

    # create the html page
    fresh_tomatoes.open_movies_page(movie_list)

if __name__ == '__main__':
    sys.exit(main())

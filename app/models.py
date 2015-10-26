import re


class Movie:
    """ Assign movie attributes """

    def __init__(self, movie):
        self.title = movie["Title"]
        self.story_line = movie["Plot"]
        self.poster_image_url = movie["Poster"]
        self.trailer_youtube_url = movie["Trailer"]
        self.year = movie["Year"]
        self.rated = movie["Rated"]
        self.runtime = movie["Runtime"]
        self.youtube_id = extract_youtube_id_from_url(movie["Trailer"])


def extract_youtube_id_from_url(movie_url):
    youtube_id_match = re.search(
        r'(?<=v=)[^&#]+', movie_url)
    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', movie_url)
    trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                          else None)
    return trailer_youtube_id

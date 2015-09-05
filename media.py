import webbrowser


class Movie():
    """ Assign movie attributes """

    def __init__(self, movie):
        self.title = movie["Title"]
        self.story_line = movie["Plot"]
        self.poster_image_url = movie["Poster"]
        self.trailer_youtube_url = movie["Trailer"]
        self.year = movie["Year"]
        self.rated = movie["Rated"]
        self.runtime = movie["Runtime"]

import webbrowser       #Have a function 'open' to open a browser

class Movie():
    """A class that can create a instance to save movie information.
    Need three parameters: 'movie_title', 'image_url', 'trailer_url'.
    Also have a function 'show_trailer', used to show trailer on YouTube."""
    def __init__(self, movie_title, image_url, trailer_url):
        self.title = movie_title
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)       #show trailer on YouTube
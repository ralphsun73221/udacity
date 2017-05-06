import webbrowser

class Movie():
    def __init__(self, movie_title, movie_story, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
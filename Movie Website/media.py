import webbrowser
class Movie():
    """
    This class defines the basic structure of Movie objects.
    """
    
    def __init__(self, movie_title, movie_storyline, director_name, poster_image, youtube_trailer):
        """
        This constructor method takes 5 strings as input, This function does not return anything.
        1 --> Movie Title
        2 --> Storyline
        3 --> Director Name
        4 --> Link to poster Image
        5 --> Link to youtube trailer
        
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.director = director_name
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
    
    def show_trailer(self):
        """
        This fuction does not take any input and opens youtube trailer of the movie instance for which this fuction is called.
        """
        webbrowser.open(self.trailer_youtube_url)
        
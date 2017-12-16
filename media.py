class Movie:
    ''' This class represents a movie.

    Attributes:
        title(string): Title of movie
        poster_image_url(string): Url of movie poster image
        trailer_youtube_url(string): Youtube url of movie trailer

    '''

    def __init__(self, title, poster, trailer):
        '''Constructor method for Movie class

        Inputs:
            title(string): Title of movie
            poster: Url of movie poster image
            trailer: Youtube url of movie trailer
        '''

        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

#!/usr/bin/env python

# standard library imports
import webbrowser

# third party imports for movie webpage
#  n/a
# local application/library specific imports
#  n/a

"""       media:
            Creates Movie Class to hold following movie specific information:
                        1.title, 2. storyline, 3.poster_image_url,
                        4.trailer_youtube_url, 5.rating
            implements show_trailer() method
"""
__author__ = "Chandra SRK "
__copyright__ = "Copyright 2017,The Project MLFND-PF-mlfnd_MovieTrailerWebsite"
__credits__ = [" ", " "]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chandra SRK"
__email__ = ""
__status__ = "Alpha"


#  Class Defition for Movie
class Movie:
    """This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

# method - constructor
    def __init__(
                self,
                movie_title,
                movie_storyline,
                movie_poster_image_url,
                movie_trailer_youtube_url,
                rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
        self.rating = rating

# method - show_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
# end of Media

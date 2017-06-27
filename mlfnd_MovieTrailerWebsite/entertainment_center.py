#!/usr/bin/env python

# standard library imports

# third party imports for movie webpage
import fresh_tomatoes

# local application/library specific imports
import media

"""     entertainment_center: creates Movie instances and associates Movies to
        Movie Database.
        Then Opens the Movie Webpage to display Movie Trailers to allow user
        to play selected trailer.
"""
__author__ = "Chandra SRK "
__copyright__ = "Copyright 2017, The Project MLFND-PF"
__credits__ = [" ", " "]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chandra SRK"
__email__ = ""
__status__ = "Alpha"

toy_story = media.Movie(
            "Toy Story",
            "A Story of a boy and his toys that come to life",
            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
            "https://www.youtube.com/watch?v=vwyZH85NQC4",
            media.Movie.VALID_RATINGS[0]
                )
avatar = media.Movie(
            "Avatar",
            "A marine on an alien planet",
            "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
            "http://www.youtube.com/watch?v=-9ceBgWV8io",
            media.Movie.VALID_RATINGS[2]
                )
dj = media.Movie(
            "DJ",
            "Gudilo Badilo Madilo Vodilo Full Song",
            "https://naasongs.com/wp-content/uploads/2017/06/DJ-Duvvada-Jagannadham-2017.jpg",  # noqa
            "https://www.youtube.com/watch?v=ul-YyTYvIRE&spfreload=5",
            media.Movie.VALID_RATINGS[0]
            )

movieDbList = [toy_story, avatar, dj]
print("Movie Server info:")
print(" "*4 + "Number of Movies:" + str(len(movieDbList)))

fresh_tomatoes.open_movies_page(movieDbList)
print("Movie Server Started .")


# end of entertainment_center

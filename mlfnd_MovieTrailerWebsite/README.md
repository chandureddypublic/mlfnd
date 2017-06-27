MLFND-Module1-P1: Movie Trailer

Overview:
  This is sample Movie Trailer Website to dislay list of favorite movies and watch the trailers.

Pre-requisites:
    intsall Python 2.7
    
Quick Start:
    Download the code  from : https://github.com/chandureddypublic/mlfnd/new/master/mlfnd_MovieTrailerWebsite
    extract the content to mlfnd_MovieTrailerWebsite
    Run the application:python entertainment_center.py, to open the webpage displaying Movie Trailer List
    Click on the Movie Tile to see trailer in youtube.

Sources:
    README.md -  This file containing overview of this Project.
    media.py - Contains the class that provides the data structure to hold movie information.
    entertainment_center.py - Pythin application which builds the movie instances and then movie list. 
                              Then it calls the method to generate the movie trailer web page.
    fresh_tomatoes.py- This is re-used web page generator. 
                        It takes list of movies created by entertainment_center.py and builds the HTML and opens up
                        the default browser to display the already generated HTML page.

Open Issues:
   N/A

TODO:
1. Writing Own Webpage generator instead of fresh_tomatoes.py
2. Error Handling for all API in  fresh_tomatoes.py
3. Exception Handling for all API in  fresh_tomatoes.py
4. Addtional info display in webpage like : Movile Story line, Rating

# MLFND-Module1-P1: Movie Trailer <h1>
## 1.Overview: <h2>
  This is sample Movie Trailer Website to dislay list of favorite movies and watch the trailers.
  
## 2.Pre-requisites: <h2>
  intsall Python 2.7
    
## 3.Quick Start: <h2>
    3.1. Download the code  from : https://github.com/chandureddypublic/mlfnd/new/master/mlfnd_MovieTrailerWebsite
    3.2. extract the content to mlfnd_MovieTrailerWebsite
    3.3. Run the application:python entertainment_center.py, to open the webpage displaying Movie Trailer List
    3.4  Click on the Movie Tile to see trailer in youtube.

## 4.Sources:<h2>
    README.md -  This file containing overview of this Project.
    media.py - Contains the class that provides the data structure to hold movie information.
    entertainment_center.py - Pythin application which builds the movie instances and then movie list. 
                              Then it calls the method to generate the movie trailer web page.
    fresh_tomatoes.py- This is re-used web page generator. 
                        It takes list of movies created by entertainment_center.py and builds the HTML and opens up
                        the default browser to display the already generated HTML page.

## 5.Open Issues:<h2>
   N/A

## 6.TODO:<h2>
1. Writing Own Webpage generator instead of fresh_tomatoes.py
2. Error Handling for all API in  fresh_tomatoes.py
3. Exception Handling for all API in  fresh_tomatoes.py
4. Addtional info display in webpage like : Movile Story line, Rating

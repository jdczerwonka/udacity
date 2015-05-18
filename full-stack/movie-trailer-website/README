Project Title: Movie Trailer Website
Project Purpose: To complete the first project requirements for the Full Stack Web Developer Nanodegree as laid out by Udacity.
Project Description: This project takes a list of movie and television id's from themoviedb.org and uses its corresponding API 
to pull relevant details related to the content and stores that data in a class.  From this list of classes, two webpages are 
dynamically generated using preconfigured content provided by Udacity which was further edited by the author.  The webpages 
are stored in the same location as the python scripts and one is automatically opened on the users computer.
Module Connections: my_entertainment_center.py references create_media.py and my_favorites.py.  It is the only script that
needs to be run to generate the webpages.

Project Contents:
create_media.py
Description: This python script is similar to the media.py script that was created in class.  It now contains two classes, one
for television and one for movies (although currently the classes are almost identical, I separated them as a tv series and a 
movie are inherently different content types with some key differences that, while not utilized now, may be used in the future).
This module also contains various functions to make API calls to themoviedb.org and parse the correpsonding json results.

my_entertainment_center.py
Description: This python script is similar to the entertainment_center.py script that was created in class.  Instead of passing
the class arguments to create_media.py (media.py in the original), it passes themoviedb.org id's which are stored in a 
dictionary.  The keys to this dictionary are largely irrelevant and serve mostly as a function to provide a description of the
content to anyone reading this program.  Instances of both classes (Movie and Television) are then stored in respective lists
which are then passed to my_favorites.py (fresh_tomatoes.py in the original).

my_favorites.py
Description:  This python script is similar to the fresh_tomatoes.py script given out in class.  This modules takes the lists
generated in my_entertainment_center.py (entertainment_center.py in the original) and creates the correspondings html, css, and
javascript to present the contents of the classes from create_media.py (media.py in the original) in an interesting and 
visually appealing manner.  Changes were made to the navbar to make it more dynamic/responsive especially accounting for the 
fact that I added another element to the nav list (in addition to my favorite movies, there is now my favorite Television).  
Consequently, I second html page had to be generated, and this program was altered to account for that.  Because of personal 
preference, I separated out the custom css and javascript that was originally supposed to be in the html header into their own
separate files.  Additionally, the user will see an overview of the plot in a popover whenever they hover over the title of
the content.

The folowing files are examples from previously generated scripts.  There contents will be overwritten if the scripts are reran.
main.css
Description: Provides additional styling beyond what is provided by the references to the bootstrap framework.

movie.html
Description: An html document containing the information for my favorite movies.

tv.html
Description: An html document containing the information for my favorite tv series.

modal.js
Description: Provides additional javascript/jquery beyond what is provided by the references to the bootstrap framework.

Author: Jonathan D. Czerwonka

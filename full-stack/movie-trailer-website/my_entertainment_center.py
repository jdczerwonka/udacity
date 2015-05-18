import create_media
import my_favorites

# The values in movie_dict are themoviedb.org id's that will be used in the API
# call query the relevant information about the movies.  The keys in this dictionary
# are to provide the reader with an easy understanding of the content available.
movie_dict = {'Avengers': 24428, 'Avengers:Age of Ultron': 99861,
              'Thor': 10195, 'Thor:The Dark World': 76338,
              'Captain America:The First Avenger': 1771, 'Captain America:The Winter Soldier': 100402,
              'Iron Man': 1726, 'Iron Man 2': 10138,
              'Guardians of the Galaxy': 118340, 'The Dark Knight': 155}
movies = []

# The values in movie_dict are themoviedb.org id's that will be used in the API
# call query the relevant information about the tv series.  The keys in this dictionary
# are to provide the reader with an easy understanding of the content available.
tv_dict = {'Agents of SHIELD': 1403, 'Gotham': 60708,
           'Arrow': 1412, 'Flash': 60735}

tv_series = []

# An object of the type Movie is created from the dictionary value and appended
# to the list movies
for key in movie_dict:
    a_movie = create_media.Movie(movie_dict[key])
    movies.append(a_movie)

# An object of the type Television is created from the dictionary value and appended
# to the list tv_series
for key in tv_dict:
    a_tv_series = create_media.Television(tv_dict[key])
    tv_series.append(a_tv_series)

# The lists movies and tv_series are passed to my_favorites.create_website to create 
# the corresponding webpages
my_favorites.create_website(movies, tv_series)

import create_media
import my_favorites

movie_dict = {'Avengers': 24428, 'Avengers:Age of Ultron': 99861,
              'Thor': 10195, 'Thor:The Dark World': 76338,
              'Captain America:The First Avenger': 1771, 'Captain America:The Winter Soldier': 100402,
              'Iron Man': 1726, 'Iron Man 2': 10138,
              'Guardians of the Galaxy': 118340, 'The Dark Knight': 155}
movies = []

tv_dict = {'Agents of SHIELD': 1403, 'Gotham': 60708,
           'Arrow': 1412, 'Flash': 60735}

tv_series = []

for key in movie_dict:
    a_movie = create_media.Movie(movie_dict[key])
    movies.append(a_movie)

for key in tv_dict:
    a_tv_series = create_media.Television(tv_dict[key])
    tv_series.append(a_tv_series)
    
my_favorites.create_website(movies, tv_series)

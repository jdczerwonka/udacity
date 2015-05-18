import json
from urllib2 import Request, urlopen

API_KEY = ''
HEADERS = {'Accept': 'application/json'}

def retrieve_movie_info(tmdb_id):
    request = Request('https://api.themoviedb.org/3/movie/' + str(tmdb_id) + '?api_key=' + API_KEY, headers=HEADERS)
    response_body = urlopen(request).read()
    return response_body

def retrieve_movie_video(tmdb_id):
    request = Request('https://api.themoviedb.org/3/movie/' + str(tmdb_id) + '/videos?api_key=' + API_KEY, headers=HEADERS)
    response_body = urlopen(request).read()
    return response_body

def retrieve_tv_info(tmdb_id):
    request = Request('https://api.themoviedb.org/3/tv/' + str(tmdb_id) + '?api_key=' + API_KEY, headers=HEADERS)
    response_body = urlopen(request).read()
    return response_body

def retrieve_tv_video(tmdb_id):
    request = Request('https://api.themoviedb.org/3/tv/' + str(tmdb_id) + '/videos?api_key=' + API_KEY, headers=HEADERS)
    response_body = urlopen(request).read()
    return response_body    

def json_to_dict(response_body):
    a_dict = json.loads(response_body)
    return a_dict

class Movie():
    def __init__(self, tmdb_id):
        movie_info_dict = json_to_dict(retrieve_movie_info(tmdb_id))
        movie_video_dict = json_to_dict(retrieve_movie_video(tmdb_id))
        
        self.title = movie_info_dict[u'title']
        self.storyline = movie_info_dict[u'overview']
        self.image_url = 'https://image.tmdb.org/t/p/w500' + movie_info_dict[u'poster_path']
        self.video_url = 'https://www.youtube.com/watch?v=' + movie_video_dict[u'results'][0][u'key']

class Television():
    def __init__(self, tmdb_id):
        tv_info_dict = json_to_dict(retrieve_tv_info(tmdb_id))
        tv_video_dict = json_to_dict(retrieve_tv_video(tmdb_id))

        self.title = tv_info_dict[u'name']
        self.storyline = tv_info_dict[u'overview']
        self.image_url = 'https://image.tmdb.org/t/p/w500' + tv_info_dict[u'poster_path']
        self.video_url = 'https://www.youtube.com/watch?v=' + tv_video_dict[u'results'][0][u'key']


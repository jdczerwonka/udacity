import webbrowser
import os
import re

# Style for the page
css_content = '''
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .content-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .content-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
'''

# Script for the page
script_content = '''
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.content-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.content-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Activates the popover data-toggles
        $(document).ready(function () {
          $('[data-toggle="popover"]').popover();
        });
'''

# HTML page head
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>My Favorites!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="main.css">
    
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="modal.js"></script>
    
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">My Favorites</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            {nav_list}
          </ul>

        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->
    </nav>

    <div class="container">
      {content_tiles}
    </div>
  </body>
</html>
'''

# A single content entry html template
content_tile = '''
<div class="col-md-6 col-lg-4 content-tile text-center" data-trailer-youtube-id="{video_url}" data-toggle="modal" data-target="#trailer">
    <img src="{image_url}" width="220" height="342">
    <h2 data-toggle="popover" data-trigger="hover" data-placement="bottom" data-content="{storyline}">{content_title}</h2>
</div>
'''

# Nav list for the page
movie_nav_list = '''
    <li class="active"><a href="movie.html">Movies<span class="sr-only">(current)</span></a></li>
    <li><a href="tv.html">Television</a></li>
'''

tv_nav_list = '''
    <li><a href="movie.html">Movies</a></li>
    <li class="active"><a href="tv.html">Television<span class="sr-only">(current)</span></a></li>
'''


# Replaces the placeholders of content_tile with the appropriate values for each piece of content
def create_content_tiles(tiles):
    # The HTML content for this section of the page
    content = ''
    for tile in tiles:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', tile.video_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', tile.video_url)
        video_url = youtube_id_match.group(0) if youtube_id_match else None
                
        # Append the tile for the movie with its content filled in
        content += content_tile.format(
            content_title=tile.title.encode('ascii', 'ignore'),
            storyline=tile.storyline.encode('ascii','ignore'),
            image_url=tile.image_url,
            video_url=video_url
        )
        
    return content

# Takes a list of movies of class create_media.Movie and a list of tv series of class
# create_media.Television and creates a webpage based on each list
def create_website(movies, tv_series):
  # Creates or overwrites the files
  movie_html_file = open('movie.html', 'w')
  tv_html_file = open('tv.html', 'w')
  css_file = open('main.css', 'w')
  script_file = open('modal.js', 'w')

  # Replaces the placeholder for the content_tiles with the actual dynamically generated content
  movie_rendered_content = main_page_content.format(content_tiles=create_content_tiles(movies),nav_list=movie_nav_list)
  tv_rendered_content = main_page_content.format(content_tiles=create_content_tiles(tv_series),nav_list=tv_nav_list)    

  # Output the files
  movie_html_file.write(main_page_head + movie_rendered_content)
  movie_html_file.close()
  
  tv_html_file.write(main_page_head + tv_rendered_content)
  tv_html_file.close()

  css_file.write(css_content)
  css_file.close()

  script_file.write(script_content)
  script_file.close()

  # open the html file in the browser
  url = os.path.abspath(movie_html_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible

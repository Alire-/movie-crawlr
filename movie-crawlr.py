from flask import Flask, render_template, url_for, request
from crawl import crawl_for_movie, read_metadata

app = Flask(__name__)

@app.route('/')
def hello():
    print 'hello'
    return render_template('index.html')

@app.route('/search')
def process_search_query():
    movie_title = request.args.get('movie_title')
    if (movie_title == ""):
        return "Please entry a movie title!"
    movie_title = movie_title.lower()
    print "MOVIE TITLE", movie_title
    if not crawl_for_movie(movie_title):
        return "Movie not found!"
    casts, prod_co, sypnosis, broadcast_date, title, imdb_url = read_metadata(movie_title)
    return render_template('metadata.html', movie_title=title,
                           sypnosis=sypnosis, broadcast_date=broadcast_date,
                           casts=casts, prod_co=prod_co, imdb_link=imdb_url)

if __name__ == '__main__':
    app.run()

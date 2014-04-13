import os
from flask import Flask, render_template, url_for, request
from subprocess import call
import json

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

def crawl_for_movie(movie_title):
    write_movie_url(movie_title)
    if os.path.isfile('movie.json'):
        os.remove('movie.json')
    f = open('./imdb/movie_url.txt')
    imdb_url = f.read()
    if "False" in imdb_url:
        return False
    print "IMDB URL: ", imdb_url
    call(["scrapy", "crawl", "imdb", "-o", "movie.json", "-t", "json"])
    return True

def write_movie_url(movie_title):
    omdb_url = get_omdb_url(movie_title)
    # omdb_url = "http://www.omdbapi.com/?i=&t=the+godfather"
    print "OMDB URL", omdb_url
    call("./get_imdb_url.sh" + " " + '"' + omdb_url + '"', shell=True)
        
def get_omdb_url(movie_title):
    tokens = movie_title.split(' ')
    omdb_url = "http://www.omdbapi.com/?i=&t="
    for token in tokens:
        omdb_url += token + '+'
    return omdb_url[:-1]

def read_metadata(movie_title):
    json_data = open('movie.json')
    data = json.load(json_data)
    json_data.close()
    cast_information = data[0]["cast_information"]
    casts = ', '.join(cast_information)
    # for cast in cast_information:
    #     casts += cast + ', '
    prod_co = data[0]["production_company"]
    sypnosis = data[0]["sypnosis"]
    broadcast_date = data[0]["broadcast_date"][1]
    title = data[0]["title"]
    f = open('./imdb/movie_url.txt')
    imdb_url = f.read()
    return casts[:-1], prod_co[0], sypnosis[0], broadcast_date, title[0], imdb_url

if __name__ == '__main__':
    app.run(debug=True)

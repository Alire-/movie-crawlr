import json, os
from subprocess import call

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
    if not cast_information:
        casts = ""
    else:
        casts = ', '.join(cast_information)
        casts = casts

    prod_co = data[0]["production_company"]
    if not prod_co:
        prod_co = ""
    else:
        prod_co = prod_co[0]

    sypnosis = data[0]["sypnosis"]
    if not sypnosis:
        sypnosis = ""
    else:
        sypnosis = sypnosis[0]

    broadcast_date = data[0]["broadcast_date"]
    if not broadcast_date:
        broadcast_date = ""
    else:
        broadcast_date = broadcast_date[1]
    title = data[0]["title"]

    if not title:
        title = ""
    else:
        title = title[0]
    f = open('./imdb/movie_url.txt')
    imdb_url = f.read()
    return casts, prod_co, sypnosis, broadcast_date, title, imdb_url


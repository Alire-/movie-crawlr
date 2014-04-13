# This bash script takes in an omdbapi.com query url and processes a movie's IMDB id from omdbapi.com.
# It then writes a imdb url for the movie with its IMDB id into movie_url.txt
#!/bin/bash
URL=$1
echo "http://www.imdb.com/title/" | tr -d '\n' > ./imdb/movie_url.txt
wget $URL -qO- | tr -d '/r' | tr -d '/n' |  sed 's/.*imdbID\"\:\"//g' | sed 's/\"\,\".*//g' >> ./imdb/movie_url.txt

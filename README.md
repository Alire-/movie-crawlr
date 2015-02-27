Movie-crawlr
============

A web application that returns a movie's or TV series' IMDb metadata given its title. Built this to learn and gain familiarity with [Scrapy](http://scrapy.org), [Flask](http://flask.pocoo.org), and [Heroku](https://www.heroku.com). I built this in a weekend in April 2014 to experiement with the above technologies for the very first time, so it's very rough. Check out how I [parsed](https://github.com/staceytay/movie-crawlr/blob/master/get_imdb_url.sh) JSON then if you dare.

[http://movie-crawlr.herokuapp.com](http://movie-crawlr.herokuapp.com)

## References
* [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
* [Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html)
* [Flask Quickstart](http://flask.pocoo.org/docs/quickstart/#quickstart)
* [Jinja Template Designer Documentation](http://jinja.pocoo.org/docs/templates/)
* [Bootstrap CSS](http://getbootstrap.com/css/)
* [Google Python Style Guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
* [XPath](http://www.w3.org/TR/xpath/)
* [The Open Movie Database API](http://www.omdbapi.com/) - used this to get IMDb's movie id for queried movies.

## Problems and bugs encountered
1. Could not install Scrapy in `virtualenv`  
  * ```error: distutils.errors.DistutilsError: Setup script exited with error: command 'cc' failed with exit status 1```
  * [Solution on Stack Overflow](http://stackoverflow.com/questions/22703393/clang-error-unknown-argument-mno-fused-madd-wunused-command-line-argumen)  
2. Accidentally adding venv to git  
  * Fixed using `git reset HEAD^`  
3. Pushing to Heroku  
  * ```error: distutils.errors.DistutilsError: Setup script exited with error: command 'gcc' failed with exit status 1```
  * [Solution on Stack Overflow](http://stackoverflow.com/questions/22415725/problems-with-custom-libffi-heroku-buildpack)  
4. Bash script could not run on Heroku  
  * Substituted `wget` with `curl` in get_imdb_url.sh

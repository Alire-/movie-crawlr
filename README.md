Movie-crawlr
============

A web application that returns a movie's or TV series' meta-data given its title. Built this to learn how to use [Scrapy](http://scrapy.org), [Flask](http://flask.pocoo.org), and [Heroku](https://www.heroku.com) proper.

Link: [http://movie-crawlr.herokuapp.com](http://movie-crawlr.herokuapp.com)

## How it works
1. **Scrapy** 

## References
* [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
* [Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html)
* [Flask Quickstart](http://flask.pocoo.org/docs/quickstart/#quickstart)
* [Jinja Template Designer Documentation](http://jinja.pocoo.org/docs/templates/)
* [Bootstrap CSS](http://getbootstrap.com/css/)
* [Google Python Style Guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
  
## Problems and bugs encountered
1. Using virtualenv to install Scrapy:  
Encountered this error: distutils.errors.DistutilsError: Setup script
exited with error: command 'cc' failed with exit status 1  
[Found a solution on Stack Overflow](http://stackoverflow.com/questions/22703393/clang-error-unknown-argument-mno-fused-madd-wunused-command-line-argumen)  
2. Accidentally adding venv to git  
Fixed using `git reset HEAD^`  
3. Pushing to Heroku:  
Encountered error: distutils.errors.DistutilsError: Setup script exited with error: command 'gcc' failed with exit status 1  
This error, similar to above, occured while I was trying to push the app to Heroku.  
[Found a solution on Stack Overflow](http://stackoverflow.com/questions/22415725/problems-with-custom-libffi-heroku-buildpack)  
4. For some reason `wget` is not on Heroku, so I had to modify my shell script to use `curl` instead.

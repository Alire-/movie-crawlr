import os
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def hello():
    print 'hello'
    return render_template('index.html')

@app.route('/search')
def process_search_query():
    if request.args.get('movie_title'):
        return request.args.get('movie_title')
    return 'Oops! Something failed!'

if __name__ == '__main__':
    app.run(debug=True)

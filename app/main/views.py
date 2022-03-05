from turtle import title
from flask import render_template
from . import main
from ..requests import get_news, get_articles

# views 
@main.route('/')
def index():
    '''
    returns index page and its information
    '''
    # general_news = get_news()
    # business_news = get_news()
    # technology_news = get_news()
    
    sources = get_news()
   
    
    # title = 'Welcome to the news app.Review amazing topics'
    data = {
        'title': 'newsproject', 
        'heading': 'news'
    }
    return render_template('index.html', context=data, sources = sources)

@main.route('/news/<id>')
def articles(id):
    '''
    Display articles based on source
    '''
    # articles_source = get_articles('id')
    # business_source = get_articles('business')
    # technology_source = get_articles('technology')
    
    all_articles = get_articles(id)


    title = f'{id} Articles'
    return render_template('articles.html', articles=all_articles )


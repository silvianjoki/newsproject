from flask import render_template
from pip import main
from app import app
from ..requests import get_news, get_articles

# views 
@main.route('/')
def index():
    '''
    returns index page and its information
    '''
    general_news = get_news('general')
    business_news = get_news('business')
    technology_news = get_news('technology')
    
    title = 'Welcome to the news app.Review amazing topics'
    return render_template('index.html', title = title, general_news = general_news, business_news = business_news, technology_news = technology_news)

@main.route('/news/id')
def articles(source_id):
    '''
    Display articles based on source
    '''
    articles_source = get_articles('id')
    business_source = get_articles('business')
    technology_source = get_articles('technology')
    
    title = f'{source_id} Articles'
    return render_template('articles.html', articles_source=articles_source, business_source= business_source, technology_source=technology_source)
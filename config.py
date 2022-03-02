from ast import Pass
import os




class Config:
    '''
    Configuring the parent class-general
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}apiKey={}'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    '''
    Configuration for child class-production
    '''
    pass
    
class DevConfig(Config):
    '''
    Configuration for child class -development
    '''
    
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
import urllib.request,json
from .models import News, Articles

apiKey = None
base_url = None
articles_base_url = None

def configure_request(app):
    global apiKey, base_url, article_base_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLES_API_BASE_URL']


def get_news():
    '''function retrives json response from our api url'''
    get_news_url = base_url.format(apiKey)
    
    with urllib.request.urlopen(get_news_url) as url:  
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['sources']:   
            news_results_list = get_news_response['sources']  
            news_results = process_news(news_results_list)
            
    return news_results

def process_news(news_list):
    '''
    This function processes the results and transforms them into objects
    Args:
    news_list: dictionaries containing news details
    returns:
    returns the news_results: objects
    '''
    news_results = []
    for news_item in news_list: 
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category= news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        
        if url:
            news_object= News(id, name, description, url, category, language, country)
            news_results.append(news_object)
    return news_results

def get_articles(id):
    '''
    function gets the json respon to a url request
    '''
    get_articles_url = article_base_url.format(id, apiKey)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_details = url.read()
        get_articles_response = json.loads(get_articles_details)
        
        articles_results = None
        
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
            print (articles_results)
        return articles_results
    
def process_articles(articles_list):
    articles_results = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')
        if urlToImage:
            articles_object = Articles(author,title, description, url, urlToImage, publishedAt, content)
            articles_results.append(articles_object)
    return articles_results

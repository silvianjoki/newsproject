# model for the articles

class Articles:
    '''article class defines the article object'''
    def __init__(self, author, title, description, url, urlToImage, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content =content
        
        
# model for news 
class News:
    '''news class defines the news object'''
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id 
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.langauge = language
        self.country = country
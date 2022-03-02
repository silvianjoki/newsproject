# from typing_extensions import Self
import unittest
from app.models import News


class newsTest(unittest.TestCase):
    '''
    Test class to test behavior of news class
    '''
    def setUp(self):
        self.new_news = News('bbc-news', 'BBC News', 'Use BBC News for up-to-the-minute news, breaking news, video, audio and feature stories. BBC News provides trusted World and UK news as well as local and regional perspectives. Also entertainment, business, science, technology and health news.', '"http://www.bbc.co.uk/news"', 'general', 'en', 'gb')

    def test_instance(self):
        '''
        Test case to test if object is an instance of the class
        '''
        self.assertTrue(isinstance(self.new_news, News))

    def test_init(self):
        '''
        Test initialization tests if the object is properly initialized
        '''
        self.asserrEqual(self.new_news.id, 'bbc-news')
        self.assertEqual(self.new_news.name, 'BBC News')
        self.asserrEqual(self.new_news.description, 'Use BBC News for up-to-the-minute news, breaking news, video, audio and feature stories. BBC News provides trusted World and UK news as well as local and regional perspectives. Also entertainment, business, science, technology and health news.')
        self.asserrEqual(self.new_news.url, '"http://www.bbc.co.uk/news"')
        self.asserrEqual(self.new_news.category, 'general')
        self.asserrEqual(self.new_news.langauge, 'en')
        self.asserrEqual(self.new_news.country, 'gb')
        
        
if __name__ == '__main__':
    unittest.main
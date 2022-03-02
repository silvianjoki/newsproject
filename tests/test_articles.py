# from typing_extensions import Self
import unittest
from app.models import Articles


class articlesTest(unittest.TestCase):
    '''
    Test class to test behavior of news class
    '''
    def setUp(self):
        self.new_articles = Articles('BBC News', 'People have swapped their pens and keyboards for guns', 
        'Thousands of Ukrainian citizens are volunteering to fight, including many with no military experience.',
        'http://www.bbc.co.uk/news/world-60546011', 
        'https://ichef.bbci.co.uk/news/1024/branded_news/11C59/production/_123439727_p0brgxj5.jpg', 
        '2022-02-27T13:37:22.9175529Z'
        'As the Russian invasion continues, thousands of ordinary Ukrainians are volunteering to fight to defend their neighbourhoods, despite many having no previous military experience. \r\nMen between the ag… [+369 chars]')

    def test_instance(self):
        '''
        Test case to test if object is an instance of the class
        '''
        self.assertTrue(isinstance(self.new_articles, Articles))

    def test_init(self):
        '''
        Test initialization tests if the object is properly initialized
        '''
        self.asserrEqual(self.new_articles.author, 'BBC News')
        self.assertEqual(self.new_articles.title, 'People have swapped their pens and keyboards for guns')
        self.asserrEqual(self.new_articles.description, 'Thousands of Ukrainian citizens are volunteering to fight, including many with no military experience.')
        self.asserrEqual(self.new_articles.url, '"http://www.bbc.co.uk/news/world-60546011"')
        self.asserrEqual(self.new_articles.urlToImage, 'https://ichef.bbci.co.uk/news/1024/branded_news/11C59/production/_123439727_p0brgxj5.jpg')
        self.asserrEqual(self.new_articles.publishedAt, '2022-02-27T13:37:22.9175529Z')
        self.asserrEqual(self.new_articles.content, 'As the Russian invasion continues, thousands of ordinary Ukrainians are volunteering to fight to defend their neighbourhoods, despite many having no previous military experience. \r\nMen between the ag… [+369 chars]')

if __name__ == '__main__':
    unittest.main
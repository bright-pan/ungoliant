'''
Created on Jan 3, 2016

@author: igzo
'''

from src.model.PageExtractor import PageExtractor
import unittest
from mockito.mocking import mock
from src.model.configuration.SiteConfiguration import SiteConfiguration
from src.model.UrlFilter import UrlFilter
from src.model.fetcher.UrlFetcher import UrlFetcher
from src.model.crawler.RegularCrawler import RegularCrawler
from src.model.crawler.ComplexCrawler import ComplexCrawler
from src.model.configuration.UrlBasicConfiguration import UrlBasicConfiguration
from src.model.configuration.UrlComplexConfiguration import UrlComplexConfiguration
from src.model.Ungoliant import Ungoliant


#comenzar a testear
class UngoliantTest(unittest.TestCase):

    def setUp(self):
        self.siteMock = mock(SiteConfiguration)
        
        self.filterMock = mock(UrlFilter)
        self.fetcherMock = mock(UrlFetcher)
        self.pageMock = mock(PageExtractor)
        self.regularCrawlerMock = mock(RegularCrawler)
        self.complexConfigMock = mock(ComplexCrawler)
        
        self.basicConfigMock = mock(UrlBasicConfiguration)
        self.complexConfigMock = mock(UrlComplexConfiguration)
        
        self.sut = Ungoliant(site_config=self.siteMock, fetcher=self.fetcherMock, extractor=self.pageMock, url_filter=self.filterMock, crawler=self.regularCrawlerMock)
        self.sut.set_url_config(self.basicConfigMock)
        self.sut.set_max_crawl(1)
        
    def test_verQueSpiderInicializoCorrectamente(self):
        assert(self.siteMock.called)
    
        
    def test_crawlUnSiteConUnaConfiguracionBasicaFunciona(self):
        self.sut.crawl()
        self.regularCrawlerMock.assert_called_with(self.sut)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
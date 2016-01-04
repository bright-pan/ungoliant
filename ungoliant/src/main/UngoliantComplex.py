'''
Created on Jan 3, 2016

@author: igzo
'''

import logging

from src.model.UrlComplexConfiguration import UrlComplexConfiguration
from src.model.Ungoliant import Ungoliant
from src.model.UrlBasicConfiguration import UrlBasicConfiguration
from src.model.ComplexCrawler import ComplexCrawler
from src.main.Sites import sites
from src.model.UrlFetcher import UrlFetcher
from src.model.PageExtractor import PageExtractor

if __name__ == '__main__':
    
    logger = logging.getLogger('ungoliant')
    
    logging.basicConfig()

    logger.setLevel(logging.DEBUG)

    url_sites = sites.keys()
    site = sites[url_sites[2]]
    
    spider = Ungoliant(x_site=site.get_site())
    
    spider.set_url_config(config=site.get_config())
    spider.set_max_crawl(150)
    spider.set_crawler(ComplexCrawler())
    
    crawled = spider.crawl()
    print len(crawled)
    print crawled
'''
Created on Jan 3, 2016

@author: igzo
'''
import logging

from src.model.UrlComplexConfiguration import UrlComplexConfiguration
from src.model.Ungoliant import Ungoliant
from src.model.UrlBasicConfiguration import UrlBasicConfiguration
from src.main.Sites import sites

if __name__ == '__main__':
    
    logger = logging.getLogger('ungoliant')
    
    logging.basicConfig()

    logger.setLevel(logging.DEBUG)
    
    url_sites = sites.keys()
    site = sites[url_sites[1]]

    spider = Ungoliant(site_config=site) 

    spider.set_max_crawl(150)

    crawled = spider.crawl()
    print len(crawled)
    print crawled
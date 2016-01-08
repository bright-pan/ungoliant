'''
Created on Jan 3, 2016

@author: igzo
'''

import logging
from src.model.Ungoliant import Ungoliant
from src.main.Sites import sites
from src.model.fetcher.JSFetcher import JSFetcher


if __name__ == '__main__':

    #ver si puedo crear un modulo de logger y verificar mas paginas con js

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('ungoliant')
    
    
    url_sites = sites.keys()
    site = sites[url_sites[4]]

    #site = sites['cityboxoffice.com']
    #site = sites['engageinteractive.co.uk']
    
    spider = Ungoliant(site_config=site) 
    spider.set_max_crawl(150)
    spider.set_fetcher(JSFetcher())
    
    crawled = spider.crawl()
        
    print len(crawled)
    print crawled
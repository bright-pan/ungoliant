'''
Created on Jan 3, 2016

@author: igzo
'''

import logging
from src.model.crawler.Crawler import Crawler

class ComplexCrawler(Crawler):
    '''
    classdocs
    '''


    def __init__(self,logger=None):
        '''
        Constructor
        '''
        self.logger = logger
        
    def crawl(self, spider):

        logging.debug("Starting the crawl")

        next_page = spider.fetch(spider.get_url_config().start_url())
        
        visited = []
        visited.append(spider.get_url_config().start_url())
        
        limit = spider.get_max_crawl()

        crawled_links = []
        stack = []
        output = []
        
        while(next_page is not None and limit > 0):

            links = spider.extract_links(next_page)
            urls = spider.filter(links)

            for url in urls:
                
                if(spider.get_url_config().coincide_next_url(url) and url not in visited):
                    
                    stack.append(url)

                try:
                    if(spider.url_filter.satisfy(spider.get_url_config(), url) and url not in crawled_links):
                        
                        item = self.mark_and_scrap_url(spider, crawled_links, url)
                        limit -= 1
                        output.append(item)
                        
                    if(limit <= 0): 
                        break
                    
                except Exception as e:
                    logging.warn( "Error in first try-catch when fetching %s" % url)
            next_page = None
            
            if stack:
                next_url = stack.pop()
                visited.append(next_url)
                try:
                    next_page = spider.fetch(next_url)
                except Exception as e:
                    logging.warn( "Error in second try-catch when fetching %s" % next_url)
                    
        spider.store(output)
        spider.finish()
        
        logging.debug("Finishing the crawl")
        
        
        return crawled_links
    
    
    
    def mark_and_scrap_url(self, spider, crawled, url):

        crawled.append(url)
        content = spider.fetch(url)
        item = spider.scrap(url, content)
        
        return item
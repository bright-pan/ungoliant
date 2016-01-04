'''
Created on Jan 3, 2016

@author: igzo
'''
from src.model.Crawler import Crawler

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

        next_page = spider.fetch(spider.get_url_config().start_url())
        
        #sirve para no repetir paginas de eventos
        revised = []
        revised.append(spider.get_url_config().start_url())
        
        #maximo de paginas a crawlear
        limit = spider.get_max_crawl()

        crawled_links = []
        stack = []
        output = []
        
        while(next_page is not None and limit > 0):

            links = spider.extract_links(next_page)
            urls = spider.filter(links)

            for url in urls:
                
                if(spider.get_url_config().coincide_next_url(url) and url not in revised):
                    
                    stack.append(url)

                try:
                    if(spider.url_filter.satisfy(spider.get_url_config(), url) and url not in crawled_links):
                        
                        item = self.mark_and_scrap_url(spider, crawled_links, url)
                        limit -= 1
                        output.append(item)
                        
                    if(limit is 0): 
                        break
                    
                except Exception as e:
                    #spider.logger.warn( "Error when fetching %s" % url)
                    print "Error when fetching %s" % url
            next_page = None
            
            if stack:
                next_url = stack.pop()
                revised.append(next_url)
                try:
                    next_page = spider.fetch(next_url)
                except Exception as e:
                    #spider.logger.warn( "Error when fetching %s" % next_url)
                    print "Error when fetching %s" % url
                    
        spider.store(output)
        return crawled_links
    
    
    
    def mark_and_scrap_url(self, spider, crawled, url):

        crawled.append(url)
        page = spider.fetch(url)
        item = spider.scrap(url, page)
        
        return item
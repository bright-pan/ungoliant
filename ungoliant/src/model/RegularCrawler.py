'''
Created on Jan 3, 2016

@author: igzo
'''
from src.model.Crawler import Crawler

class RegularCrawler(Crawler):
    '''
    classdocs
    '''


    def __init__(self, logger=None):
        '''
        Constructor
        '''
        self.logger = logger
    
    def crawl(self, spider):
        
        stack = []
        crawled_links = []
        revised = []

        start_urls = spider.get_urls(spider.get_url_config().start_url())
        
        for url in start_urls:
            stack.append(url)

        output = []
        limit = spider.get_max_crawl()

        while len(stack) > 0 and limit > 0:
        
            new_url = stack.pop()

            try:
                if(spider.url_filter.satisfy(spider.get_url_config(), new_url) and new_url not in crawled_links):
                    
                    crawled_links.append(new_url)
                    limit -= 1

                    content = spider.fetch(new_url)
                    item = spider.scrap(new_url, content)
                    revised.append(new_url)
                    output.append(item)
                
                    links = spider.extract_links(content)
                    urls = spider.filter(links)
                
                    for url in urls:    
                        stack.append(url)

            except Exception as e:
                #spider.logger.warn( "Error when fetching %s" % url)
                print "Error when fetching %s" % url

        spider.store(output)
        return crawled_links
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

        start_urls = spider.get_urls(spider.url_configuration.start_url())
        
        for url in start_urls:
            stack.append(url)

        output = []
        limit = spider.get_max_crawl()

        while len(stack) > 0 and limit > 0:
        
            new_url = stack.pop()
            print "Trying to get: " + new_url

            try:
                if(spider.url_filter.satisfy(spider.url_configuration, new_url) and new_url not in crawled_links):
                    
                    print "Getting :" + new_url
                    crawled_links.append(new_url)
                    limit -= 1
                    
                    content = spider.fetch(new_url)
                    item = spider.scrap(new_url, content)

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
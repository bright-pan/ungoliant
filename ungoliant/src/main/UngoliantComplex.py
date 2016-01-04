'''
Created on Jan 3, 2016

@author: igzo
'''

from src.model.Ungoliant import Ungoliant
from src.model.ComplexCrawler import ComplexCrawler
from src.main.Sites import sites


if __name__ == '__main__':

    url_sites = sites.keys()
    site = sites[url_sites[0]]
    
    spider = Ungoliant(site_config=site)
    
    spider.set_max_crawl(150)
    spider.set_crawler(ComplexCrawler())
    
    crawled = spider.crawl()
    print len(crawled)
    print crawled
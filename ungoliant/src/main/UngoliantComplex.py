'''
Created on Jan 3, 2016

@author: igzo
'''
from src.main.Sites import sites
from src.model.Ungoliant import Ungoliant
from src.model.fetcher.JSFetcher import JSFetcher
from src.model.crawler.ComplexCrawler import ComplexCrawler




if __name__ == '__main__':

    url_sites = sites.keys()
    site = sites[url_sites[1]]
    
    spider = Ungoliant(site_config=site)
    
    spider.set_max_crawl(150)
    spider.set_crawler(ComplexCrawler())
    spider.set_fetcher(JSFetcher())
    
    crawled = spider.crawl()
    print len(crawled)
    print crawled
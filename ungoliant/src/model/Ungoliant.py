from src.model.fetcher.UrlFetcher import UrlFetcher
from src.model.PageExtractor import PageExtractor
from src.model.UrlFilter import UrlFilter
from src.model.crawler.RegularCrawler import RegularCrawler


class Ungoliant:
    
    def __init__(self, site_config, logfile=None, logger=None, fetcher=UrlFetcher(), extractor=PageExtractor(), url_filter=UrlFilter(),crawler=RegularCrawler(), scraper=None, storer=None):
        
        self.logfile = logfile
        self.logger =  logger

        self.site_config = site_config

        self.max_crawl = 0

        self.proxies = None

        self.fetcher = fetcher
        self.extractor = extractor
        self.url_filter = url_filter
        self.crawler = crawler

        self.scraper = scraper
        self.storer = storer
        
        self.crawled_urls = []
            
    def fetch(self, url):
        '''
        Recibe una url y devuelve un string con el contenido. 
        '''
        # falta el manjo del contenido dynamico ( javascript ) que aveces completa el DOM. Hay que usar phantomjs
        
        return self.fetcher.fetch(url)

    def extract_links(self, content):
        '''
        Recibe el contenido de una url y saca todos los links. Algunos de estos links, no van a ser interesantes ( no conducen a eventos ) 
        '''
        return self.extractor.extract_links(content)     
    
    def filter(self, links):
        '''
        La idea es retornar una lista filtrada de links donde solo pasan los links que son 
        relevantes al arbol de navegacion. Es decir, que cumplen con la base_url regexp. 
        '''
        # aca hay que usar una REGEXP
        #tendria que usar una condicion o una regexp en lugar de la url_configuration
        
        return self.url_filter.filter(self.site_config.get_config(), links)
   
    def get_urls(self, start_url):
        '''
        @return: una lista con los urls que se encuentran en start_url y que cumplan con una condicion
        '''
        content = self.fetch(start_url)
        start_urls = []
        if(content):
            start_links = self.extract_links(content)
            start_urls = self.filter(start_links)
        
        return start_urls

    def set_site(self, site_configuration):
        self.site_conf = site_configuration

    def set_url_config(self, config):
        '''
        @param config: is a UrlConfiguration
        '''
        self.site_config.set_config(config)
    
    def get_url_config(self):
        return self.site_config.get_config()
    
    def set_proxy(self, proxy):
        '''
        @param proxy: is a mapping, key: string protocol , value: string IP. Example = {'http' : '192.168.1.1'} 
        '''
        self.fetcher.set_proxy(proxy)
    
    def store(self, output):
        #self.storer.store(output)
        pass
    
    def scrap(self, url, page):
        #self.scraper.scrap(url,page)
        pass
    
    def set_fetcher(self, url_fetcher):
        self.fetcher=url_fetcher
    
    def set_crawler(self, crawler):
        self.crawler = crawler

    def set_max_crawl(self, max_links):
        '''
        @param max_links: es un entero, que representa el numero maximo de paginas a crawlear 
        '''
        self.max_crawl = max_links
    
    def get_max_crawl(self):
        return self.max_crawl
    
    def finish(self):
        self.fetcher.finish()
    
    def crawl(self):
        '''
        el metodo crawl realiza crawling y scraping
        '''
        self.crawled_urls = self.crawler.crawl(self)
        return self.crawled_urls
        
import logging
from UrlFetcher import UrlFetcher
from PageExtractor import PageExtractor
from UrlFilter import UrlFilter
from RegularCrawler import RegularCrawler


logger = logging.getLogger('ungoliant')

#tengo que hacer test y cambiar la clase urlfilter 


class Ungoliant:
    
    def __init__(self, site_config, fetcher=UrlFetcher(), extractor=PageExtractor(), url_filter=UrlFilter(),crawler=RegularCrawler()):
        self.logfile  = None
        self.logger =  logger

        #self.site_conf = site_config
        self.site = site_config.get_site()
        self.url_configuration = site_config.get_config()

        self.max_crawl = 0

        self.proxies = None

        self.fetcher = fetcher
        self.extractor = extractor
        self.url_filter = url_filter
        self.crawler = crawler
        
        
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
        
        return self.url_filter.filter(self.url_configuration, links)
   
    #dada una configuracion extrae esas urls
    def get_urls(self, start_url):
        '''
        @return: a list of urls
        '''
        start_urls = []
        content = self.fetch(start_url)
        if content is not None:
            start_links = self.extract_links(content)
            start_urls = self.filter(start_links)
        return start_urls

    def set_url_config(self, config):
        '''
        @param config: is a UrlConfiguration
        '''
        self.url_configuration = config
    
    def set_proxy(self, proxy):
        '''
        @param proxy: is a mapping, key: string protocol , value: string IP. Example = {'http' : '192.168.1.1'} 
        '''
        self.fetcher.set_proxy(proxy)
    
    def store(self, output):
        pass

    #duda recibe el contenido de una pagina?
    def scrap(self, url, page):
        pass
    
    def set_crawler(self, crawler):
        self.crawler = crawler

    def set_max_crawl(self, max_links):
        self.max_crawl = max_links
    
    def get_max_crawl(self):
        return self.max_crawl
    
    def crawl(self):
        '''
        el metodo crawl realiza crawling y scraping
        '''
        return self.crawler.crawl(self)
            
        
if __name__ == '__main__':
    
    #no se usa pero perdi la info de los logs

    logging.basicConfig()

    logger.setLevel(logging.DEBUG)
    
    x_site = "theindependentsf.com"
    
    spider = Ungoliant(x_site=x_site)
    spider.crawl()
'''
Created on Dec 29, 2015

@author: igzo
'''
import urllib2
import chardet
import logging
from src.model.fetcher.Fetcher import Fetcher
from src.model.exception.DecodeException import DecodeException
from src.model.exception.FetchException import FetchException


class UrlFetcher(Fetcher):
    '''
    classdocs
    '''

    def __init__(self, proxy={}):
        '''
        Constructor
        '''
        self.proxy  = proxy
        
    def set_proxy(self, proxy):
        self.proxy = proxy

    def create_request(self, url):
        
        current_headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30', 'Content-Type' : " application/x-www-form-urlencoded;charset=utf-8"}
     
        return urllib2.Request(url, headers=current_headers)
    
    
    def init_opener(self):
        '''
        Inicializa el opener que se va a usar en el fetch
        '''
        
        opener = urllib2.build_opener()
        if(self.proxy):
            proxy = urllib2.ProxyHandler(self.proxy)
            opener = urllib2.build_opener(proxy)


        #no los agrego en el opener porque ya los agrego en el request            
        #opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30")]
        #opener.addheaders = [('Accept-Charset', 'utf-8')]
        opener.addheaders = [('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
        
        urllib2.install_opener(opener)
    
    
    def decode(self, page_content):
        '''
        @return: a decoded page
        '''
        encoding = chardet.detect(page_content)
        try:
            return page_content.decode(encoding['encoding'])
        except:
            raise DecodeException("Error trying to decode page in utf-8") 
    
    
    def fetch(self, url):
        '''
        Recibe una url y devuelve un string con el contenido. 
        '''        
        self.init_opener()
        if not url:
            raise Exception("URL can not be null")

        logging.debug( "About to fetch url %s" % url)
                
        req = self.create_request(url)
        
        try:
            response = urllib2.urlopen(req)
            content  = response.read()
            response.close()
        except FetchException:
            logging.warn("Error in fetch: %s" %url)
            raise FetchException("Error trying to fetch %s" % url)
        try:
            decoded = self.decode(content)
            return decoded
        except DecodeException:
            logging.warn("Error trying to decode %s" % url)
            return None
        
    def finish(self):
        pass
        

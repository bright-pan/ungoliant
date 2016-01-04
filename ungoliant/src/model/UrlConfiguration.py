'''
Created on Dec 19, 2015

@author: igzo
'''
import urlparse

class UrlConfiguration(object):
    '''
    classdocs
    '''


    def __init__(self, start='', base= ''):
        '''
        Constructor
        '''
        self.start = start
        self.base = base
                
    def start_url(self):
        return self.start
    
    def base_url(self):
        return self.base
    
    def full_url(self, url):
        return urlparse.urljoin(self.base_url(), url)
    
    def key_url(self):
        raise NotImplementedError("Abstract method")
    
    def next_url(self):
        raise NotImplementedError("Abstract method")
    
    def coincide_next_url(self):
        raise NotImplementedError("Abstract method")
    

'''
Created on Dec 19, 2015

@author: igzo
'''
from src.model.configuration.UrlConfiguration import UrlConfiguration

class UrlComplexConfiguration(UrlConfiguration):
    '''
    classdocs
    '''


    def __init__(self, start='', base= '', key='', following=''):
        '''
        Constructor
        '''
        UrlConfiguration.__init__(self, start, base)
        self.key = key
        self.following = following
        
    def key_url(self):
        return self.key
        
    def next_url(self):
        return self.following
    
    def coincide_next_url(self, url):
        return self.following in url
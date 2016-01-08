'''
Created on Dec 19, 2015

@author: igzo
'''
from src.model.configuration.UrlConfiguration import UrlConfiguration

class UrlBasicConfiguration(UrlConfiguration):
    '''
    classdocs
    '''
    def __init__(self, start='', base= '', key=''):
        '''
        Constructor
        '''
        UrlConfiguration.__init__(self, start, base)
        self.key = key
    
    def key_url(self):
        return self.key
    
    def next_url(self):
        return ''
    
    def coincide_next_url(self, url):
        return False
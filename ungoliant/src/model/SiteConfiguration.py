'''
Created on Jan 3, 2016

@author: igzo
'''

class SiteConfiguration(object):
    '''
    classdocs
    '''


    def __init__(self, site=None, url_config=None):
        '''
        Constructor
        '''
        self.site = site
        self.url_config = url_config
        
    def get_site(self):
        return self.site
    
    def get_config(self):
        return self.url_config
    
    def set_site(self, site):
        self.site = site
        
    def set_config(self, url_config):
        self.url_config = url_config
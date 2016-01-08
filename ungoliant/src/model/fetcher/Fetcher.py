'''
Created on Jan 8, 2016

@author: igzo
'''

class Fetcher(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def fetch(self, url):
        raise NotImplementedError("Abstract method")
        
    def set_proxy(self, proxy):
        raise NotImplementedError("Abstract method")
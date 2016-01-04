'''
Created on Jan 3, 2016

@author: igzo
'''

class Crawler(object):


    def __init__(self,logger=None):
        '''
        Constructor
        '''
        self.logger = logger
    
    def crawl(self, spider):
        raise NotImplementedError("Abstract method")
'''
Created on Dec 29, 2015

@author: igzo
'''

class UrlFilter(object):
    '''
    classdocs
    '''    
    

    def satisfy(self, url_config, url):
        return url_config.key_url() in url and url_config.base_url() in url
    
    
    def filter(self, url_config, links):
        '''
        La idea es retornar una lista filtrada de links donde solo pasan los links que son 
        relevantes al arbol de navegacion. Es decir, que cumplen con la base_url regexp. 
        '''
        # aca hay que usar una REGEXP
    
        url_list = []
        
        for link in links:
            #should be a regexp
            url = link['href']
            full_url = url_config.full_url(url)
            if self.satisfy(url_config, full_url):
                url_list.append(full_url)
        return url_list
'''
Created on Dec 29, 2015

@author: igzo
'''
from bs4 import BeautifulSoup

class PageExtractor(object):
    '''
    classdocs
    '''
    
    def extract_links(self, page_content):
        '''
        Recibe el contenido de una pagina y saca todos los links. Algunos de estos links, no van a ser interesantes ( no conducen a eventos ) 
        '''
        soup = BeautifulSoup(page_content)
        links = soup.find_all('a', {'href' : True})
        
        return links
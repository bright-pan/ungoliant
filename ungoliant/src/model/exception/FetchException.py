'''
Created on Dec 31, 2015

@author: igzo
'''

#problem con esto es que engloba todas las excepciones que puedan ocurrir en un fetch de una url, es decir
#no es especifico

class FetchException(Exception):
    '''
    this class include all errors what occurs in fetch
    '''
    def __init__(self, errorMessage):
        self.__init__(errorMessage)
        
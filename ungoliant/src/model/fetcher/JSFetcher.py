'''
Created on Jan 4, 2016

@author: igzo
'''
import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from src.model.fetcher.Fetcher import Fetcher

class JSFetcher(Fetcher):
    '''
    classdocs
    '''


    def __init__(self, proxy=None):
        '''
        Constructor
        @param proxy: es un string de una direccion ip. ex: "192.168.0.1"
        '''
        self.current_proxy = proxy
        self.driver = None

    
    def fetch(self, url):
        
        #elegir un tiempo de espera mas corto o arreglar el tiempo de espera implicito o usar correctamente el webdriverwait
        
        self.driver = self.initialize_phantom()
        logging.debug("About to fetch url %s" % url)
        try:
            self.driver.get(url)
            sleep(3)
            #element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "myDinamicElement")))
            html = self.driver.page_source        
            content = html.encode("utf-8")
            return content

        except TimeoutException as e:
            logging.warn("url can not be loaded correctly: %s" %url)
            return None
        except Exception as e:
            logging.warn("Error at fetching with phantomjs")
            return None

    def set_proxy(self,proxy):
        
        protocol = proxy.keys()[0]
        ip = proxy[protocol]
        self.current_proxy = ip
        self.driver.setProxy(ip)   
        
    def initialize_phantom(self):
        
        capabilities = dict(DesiredCapabilities.PHANTOMJS)
        #capabilities["phantomjs.page.settings.resourceTimeout"] = 1000
        capabilities["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 " "(KHTML, like Gecko) Chrome/15.0.87")
        services = None
        if(self.current_proxy):
            services = ['--proxy=' + self.current_proxy ,'--proxy-type=http',]
        driver = webdriver.PhantomJS(desired_capabilities=capabilities, service_args=services)
        
        #driver.implicitly_wait(3)
        #driver.set_page_load_timeout(3)
        
        return driver
    
    def finish(self):
        self.driver.close()
        self.driver.quit()
        
        
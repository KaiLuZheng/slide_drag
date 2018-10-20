#/usr/bin/python3


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time
import sys
import logging

headers = {}
headers['User-Agent'] ='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'

class selereq():
    def __init__(self):
        chrome_options = Options()       
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        # can be changed by functions, now do not
        for i in headers:
            chrome_options.add_argument(i + '="' + headers[i] + '"')

        self.chrome_options = chrome_options
        self.opener = webdriver.Chrome(chrome_options = chrome_options)
        self.waittime = 5
        self.frequence = 0.5

    def get_openurl(self, url):
        self.opener.get(url)

    def quit(self):
        self.opener.close()
        self.opener.quit()
        
    def wait_EC_locator(self, EC_locator):
        # maybe timeout
        element = WebDriverWait(self.opener, self.waittime, self.frequence).until(EC_locator)
        return element

    def sendkeys_byid(self, iditem, keys):
        self.opener.find_element_by_id(iditem).clear()
        self.opener.find_element_by_id(iditem).send_keys(keys)

    def click_byid(self, iditem):
        self.opener.find_element_by_id(iditem).click()

    
    def element_by_xpath(self, strings):
        return self.opener.find_element_by_xpath(strings)


    def element_by_id(self, iditem):
        return self.opener.find_element_by_id(iditem)

    def switch2frame(self, iframe):
        self.opener.switch_to.frame(iframe)

    def switch2upper(self):
        self.opener.switch_to.parent_frame()
   
    def check_source(self):
        return self.opener.page_source

    def openerBody(self):
        return self.opener
 
    def check_byclass(self, classItem):
        try:
            item = self.opener.find_element_by_class_name(classItem).text
            return True
        except Exception as e:
            logging.error('find class.error: %s'%e)
            return False

    def openerAction(self):
        return ActionChains(self.opener)



if __name__ == '__main__':
    a = selereq()

    a.get_openurl('http://news.qq.com/')
    a.quit() 

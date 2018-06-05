from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from utilities.Locators import Locator
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from base.selenium_driver import SeleniumDriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.options import Options
import os




class login_test(unittest.TestCase):
    
    def setUp(self):
        
        #chromedriver = "C:\\Users\\apollu\\lib\\chromedriver_win32\\chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        
        #opts = ChromeOptions()                                         
        #opts.add_experimental_option("detach", True)                 
        #opts.add_argument('disable-infobars')
        #self.driver = webdriver.Chrome(chromedriver, chrome_options=opts)
        
        

        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\apollu\\lib\\chromedriver_win32\\chromedriver.exe',chrome_options=opts,)
        
        #cap = DesiredCapabilities().FIREFOX
        #cap["marionette"] = False
        #self.driver = webdriver.Firefox(capabilities=cap, executable_path='C:\\Users\\apollu\\geckodriver-v0.20.1-win64\\geckodriver.exe')
        #self.driver = webdriver.Chrome(executable_path='C:\\Users\\apollu\\lib\\chromedriver_win32\\chromedriver.exe')
        #self.driver = webdriver.Firefox(executable_path='C:\\Users\\apollu\\geckodriver-v0.20.1-win64\\geckodriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
    def test_login(self):
        self.driver.get(Locator.BaseUrl)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Locator.Username_id).send_keys(Locator.Username)
        self.driver.find_element_by_xpath(Locator.Password_id).send_keys(Locator.Password)
        self.driver.find_element_by_xpath(Locator.Login_id).click()
        self.driver.implicitly_wait(50)
        self.driver.find_element_by_xpath(Locator.click_orchestration).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector(Locator.Addworkflow).click()    
           
        
    #def tearDown(self):
        #self.driver.quit()        
        
    
        
if __name__ == "__main__":
    unittest.main()
    
    
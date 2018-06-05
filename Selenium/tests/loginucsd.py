from selenium import webdriver
import unittest
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.options import Options



class TestClass(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome('C:\\Users\\apollu\\lib\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)

    def test_loginUI(self):
# waiting for 10 secs
        self.driver.get('https://172.31.234.59/app/ui/login.jsp')
        self.driver.implicitly_wait(25)
        print(self.driver.title)
# waiting for 15 seconds to load the page
        self.driver.implicitly_wait(15)
        self.uname = self.driver.find_element_by_xpath('//*[@id="username"]')
        print(self.uname)
        self.pwd = self.driver.find_element_by_xpath('//*[@id="password"]')
        print(self.pwd)
        self.uname.send_keys("admin")
        self.pwd.send_keys("admin")
        self.submitbutton = self.driver.find_element_by_id("Submit")
        self.submitbutton.click()
        self.driver.implicitly_wait(25)
        print(self.driver.title)
        self.driver.implicitly_wait(60)
#self.orchmenu = self.driver.find_element_by_xpath('//*[@id="menuitem-1141-iconEl"]')
        self.orchmenu = self.driver.find_element_by_id('menuitem-1145-iconEl')
        self.orchmenu.click()

    #def tearDown(self):
        #self.driver.close()

if __name__ == '__main__':
    unittest.main()
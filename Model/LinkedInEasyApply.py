from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class LinkedInEasyApply:
    def __init__(self, username, password, keyword, location):
        self.username = username
        self.password = password
        self.keyword = keyword
        self.location = location

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True) # Keep the browser open after the script is done
        self.driver = webdriver.Chrome(options=options)
        self.login()
    
    def login(self):
        self.driver.get("https://www.linkedin.com/login")
        email_input = self.driver.find_element("id", "username")
        email_input.clear()
        email_input.send_keys(self.username)
        time.sleep(2)

        password_input = self.driver.find_element("id", "password")
        password_input.clear()
        password_input.send_keys(self.password)

        time.sleep(2)

        login_button = self.driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div[1]/form/div[3]/button")

        login_button.click()

        # login_button = self.driver.find_element_by_css_selector(".btn__primary--large")
        # login_button.click()        

        
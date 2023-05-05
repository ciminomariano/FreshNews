import datetime
import time
import xlsxwriter
import re
import os
import requests
from RPA.Browser import Browser

from exceptions.custom_exceptions import CustomException, log_section_not_found, log_element_not_found
from exceptions.selenium_exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta


class CustomActions:
    def __init__(self, url):
        self.browser = Browser()
        self.url = url


    def open_website(self, url):
        try:
            self.browser.open_available_browser(url)
            time.sleep(5)
            return True
        except NoSuchElementException:
            raise CustomException("We could not find any element at the page")
        except WebDriverException:
            raise CustomException("The page could not be loaded")


    def maximaze_nav(self):
        try:
            self.browser.maximize_browser_window()
            return True
        except Exception:
            raise CustomException("The Browser could not be Maximized")


    
    def accept_cookies(self):
        try:
            boton_accept = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="GDPR-accept"]'))
        )
            if boton_accept:
                boton_accept.click()
                print("Accept button Found, clicking on it")
                time.sleep(10)
                return True
        except Exception:
            raise CustomException("The element boton_aceppt from cookies"
                                  "was not found")
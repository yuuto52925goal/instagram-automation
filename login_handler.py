import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginHandler:
    def __init__(self, username, password):
        load_dotenv()
        self.username = username
        self.password = password
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com/')

    def login(self):
        time.sleep(2)
        username_input = self.driver.find_element(by=By.NAME, value="username")
        username_input.send_keys(self.username)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)

        time.sleep(4.3)
        button_save = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if button_save:
            button_save.click()

        time.sleep(4)
        button_notification = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if button_notification:
            button_notification.click()


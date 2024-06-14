from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KpiHandler:
    def __init__(self, account_name):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(f'https://www.instagram.com/{account_name}')

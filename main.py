import os
from bs4 import BeautifulSoup
import requests
import lxml
from login_handler import LoginHandler
from dotenv import load_dotenv


# response = requests.get("https://www.instagram.com/'")
# soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())

load_dotenv()
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

instagram_analyze = LoginHandler(username, password)
instagram_analyze.login()


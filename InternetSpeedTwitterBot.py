from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
from time import sleep
import os

from dotenv import load_dotenv


class InternetSpeedTwitterBot:

    def __init__(self):
        # .env file contains api keys in the format of API_KEY="xxxxxx", get it using os.environ['API_KEY']; before that pip install python-dotenv
        load_dotenv()  # take environment variables from .env.

        self.PROMISED_UP = 10
        self.PROMISED_DOWN = 100
        self.my_email = os.environ['MY_EMAIL']
        self.my_password = os.environ['TWITTER_PASS']

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import time
import pandas as pd
from tabulate import tabulate

class Inflow:
    def __init__(self):
        self.service = Service(executable_path='./chromedriver.exe')
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.exchange_rates = []  # List to store exchange rates

    def track(self):
        while True:
            self.driver.get(url="https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=PHP")

            wait = WebDriverWait(self.driver, 10)
            text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/div/p[2]'))).text
            if text == '':
                text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/div/p[2]/text()[1]'))).text
            text = re.sub("[\(\[].*?[\)\]]", "", text)
            
            text_parts = text.split()
            exchange_rate = float(text_parts[0].replace(",", ""))

            self.exchange_rates.append(exchange_rate)
            
            print(f"Current USD to PHP exchange rate: {exchange_rate}")
            time.sleep(10)

inf = Inflow()
inf.track()


import time
import datetime
import asyncio

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from telegram_bot import send_message_bot



def setup_driver(executable_path: str) -> webdriver.Chrome:
    chrome_binary_path = "/usr/bin/google-chrome"
    service = Service(executable_path)
    options = Options()
    options.binary_location = chrome_binary_path
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver


def login(driver: webdriver.Chrome, username: str, password: str):
    driver.get('https://mercury.vetrf.ru/')
    driver.find_elements(By.XPATH, '//div[@class="con-content"]//div[@class="sub-system"]/div[@class="sub-system-caption-h"]/a')[3].click()
    driver.find_element(By.NAME, 'j_username').send_keys(username) 
    password_element = driver.find_element(By.XPATH, '//input[@id="password"]') 
    password_element.send_keys(password)  
    password_element.send_keys(Keys.ENTER) 


def select_elements(driver: webdriver.Chrome): 
    driver.find_elements(By.XPATH, '//label[@class="active"]/input')[1].click() 
    driver.find_element(By.XPATH, '//button[@type="submit"]').click() 


def process_packages(driver: webdriver.Chrome): 
    number_of_packages_executed = 0 
    flag = True
    while flag:
        time.sleep(6)
        driver.find_elements(By.XPATH, '//div[@id="main-menu"]/ul/li')[6].click()
        driver.find_elements(By.XPATH, '//a[contains(text(), "Оформленные")]')[1].click()

        try:
            driver.find_element(By.XPATH, '//div[@id="listContent"]//tr[@class="second"]//a[@class="operation-link blue"]').click()
            driver.find_element(By.XPATH, '//button[@id="quenchButton"]').click()
            driver.find_element(By.XPATH, '//button[@class="positive"]').click()
            number_of_packages_executed += 1 
        except NoSuchElementException:
            current_date_time = datetime.datetime.now().strftime('%d/%m/%y (%H:%M)')
            flag = False
            text = f'''Количество погашенных пакетов - {number_of_packages_executed}\n\n{current_date_time} - Пакетное гашение закончено. Непогашенных пакетов не осталось.'''
            asyncio.run(send_message_bot(text=text))
        except Exception: 
            asyncio.run(send_message_bot(text='Что то пошло не так, и программа закрылась преждевременно!')) 
            flag = False

def main(): 
    driver = setup_driver(executable_path="/home/user/bot/chromedriver") 
    login(driver, 'your_login', 'your_password')
    select_elements(driver)
    process_packages(driver)       
    

if __name__ == "__main__": 
    main()

#h

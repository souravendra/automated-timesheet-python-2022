from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from pytz import timezone
from datetime import datetime
load_dotenv(Path('.env'))

print('TIMESHEET AUTOFILL')
driver = webdriver.Chrome(
    executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
driver.get('https://warehousenow.keka.com/')
driver.refresh()
try:
    elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login-container-center"]/div/div/form/div/div[4]/div/button')))
finally:
    emailbox = driver.find_element_by_xpath('//*[@id="email"]')
    passwordbox = driver.find_element_by_xpath('//*[@id="password"]')
    loginbutton = driver.find_element_by_xpath(
        '//*[@id="login-container-center"]/div/div/form/div/div[4]/div/button')

    emailbox.send_keys(os.getenv('EMAIL'))
    passwordbox.send_keys(os.getenv('PASSWORD'))
    loginbutton.click()
    # driver.quit()

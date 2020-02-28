from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader
import os
import time


def start_browser():
    global driver
    if (ConfigReader.read_config_data('details','Browser')) == "Chrome":
        path ="C:/Users/Dell Laptop/EndtoEndAutomation/Driver/chromedriver.exe"
        driver =Chrome(executable_path=path)

    elif(ConfigReader.read_config_data('details','Browser')) == "Firefox":
        path ="C:/Users/Dell Laptop/EndtoEndAutomation/Driver/chromedriver.exe"
        driver =Chrome(executable_path=path)

    else:
        path = "C:/Users/Dell Laptop/EndtoEndAutomation/Driver/chromedriver.exe"
        driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(ConfigReader.read_config_data('details', 'application_URL'))

    return driver


def close_browser():
    driver.close()


def implicity_wait(sec):
    driver.implicitly_wait(sec)
    return implicity_wait(sec)




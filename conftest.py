import pytest
import options
import random as r
from selenium import webdriver
from data import website
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    option.add_argument('--window-size=1920,1080')
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

#@pytest.fixture(params=['firefox', 'chrome'])
#def driver(request):
    #if request.param == 'firefox':
        #options = Options()
        #driver = webdriver.Firefox(options=options)
    #elif request.param == 'chrome':
        #option = webdriver.ChromeOptions()
        #driver = webdriver.Chrome()
    #options.add_argument('--window-size=1920,1080')
    #driver.get(website)
    #yield driver
    #driver.quit()

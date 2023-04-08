import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = None

@pytest.fixture(scope="class")
def setup(request):
    global driver
    service_obj = Service("/Users/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=service_obj)
    driver.get("https://iwanttohelp.bim.assistcloud.services/")
    driver.implicitly_wait(10)
    act = ActionChains(driver)
    wait = WebDriverWait(driver, 15)
    request.cls.driver = driver
    request.cls.act = act
    request.cls.wait = wait
    yield
    driver.close()
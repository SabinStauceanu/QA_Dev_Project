import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Headers:
    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    header1 = (By.XPATH,"//ul/li[1][@class='nav-item']")
    header2 = (By.XPATH, "//ul/li[2][@class='nav-item']")
    header3 = (By.XPATH, "//ul/li[3][@class='nav-item']")
    header4 = (By.XPATH, "//ul/li[4][@class='nav-item']")
    header5 = (By.XPATH, "//ul/li[5][@class='nav-item']")
    header6 = (By.XPATH, "//ul/li[6][@class='nav-item']")
    header7 = (By.XPATH, "//ul/li[7][@class='nav-item']")

    def getAcasa(self):
        self.wait.until(expected_conditions.element_to_be_clickable((Headers.header1)))
        return self.driver.find_element(*Headers.header1)

    def getTopVoluntari(self):
        self.wait.until(expected_conditions.element_to_be_clickable((Headers.header2)))
        return self.driver.find_element(*Headers.header2)

    def getListaNevoi(self):
        self.wait.until(expected_conditions.element_to_be_clickable((Headers.header3)))
        return self.driver.find_element(*Headers.header3)

    def getDespreNoi(self):
        self.wait.until(expected_conditions.element_to_be_clickable((Headers.header4)))
        return self.driver.find_element(*Headers.header4)

    def getOfertaSugestie(self):
        self.wait.until(expected_conditions.element_to_be_clickable((Headers.header5)))
        return self.driver.find_element(*Headers.header5)

    def getDevinoVoluntar(self):
        self.wait.until(expected_conditions.element_to_be_clickable((Headers.header6)))
        return self.driver.find_element(*Headers.header6)

    def getAutentificare(self):
        self.wait.until(expected_conditions.element_to_be_clickable((Headers.header7)))
        return self.driver.find_element(*Headers.header7)

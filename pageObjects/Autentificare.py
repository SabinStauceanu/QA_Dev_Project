import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Autentificare():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    nrTel = (By.NAME, "phone_number")
    password = (By.NAME, "password")
    btnDisconnect = (By.XPATH, "")
    brnAuth = (By.CSS_SELECTOR, "button[type='submit']")
    btnDisconnect = (By.XPATH, "//li[8]")
    eroare = (By.XPATH, "//div/span")

    def getTel(self):
        self.driver.find_element(*Autentificare.nrTel).clear()
        return self.driver.find_element(*Autentificare.nrTel)

    def getPass(self):
        self.driver.find_element(*Autentificare.password).clear()
        return self.driver.find_element(*Autentificare.password)

    def getAuth(self):
        return self.driver.find_element(*Autentificare.brnAuth)

    def getDisconnect(self):
        return self.driver.find_element(*Autentificare.btnDisconnect)

    def getEroare(self):
        self.wait.until(expected_conditions.presence_of_element_located((Autentificare.eroare)))
        return self.driver.find_element(*Autentificare.eroare)
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class TopVoluntariPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    voluntari = (By.XPATH,"//div[@class='card-body']/div/div/div")
    buttonVoluntari = (By.CSS_SELECTOR, "button[role$='menuitem']")
    buttonZoomIn = (By.XPATH, "//div[3]/div/button[1]")
    buttonZoomOut = (By.XPATH, "//div[3]/div/button[1]")
    harta = (By.CSS_SELECTOR, "div[id='search-map']")

    def getVoluntari(self):
        time.sleep(1)
        Voluntari = self.driver.find_elements(*TopVoluntariPage.voluntari)
        if self.driver.find_element(*TopVoluntariPage.buttonVoluntari).is_enabled():
            time.sleep(1)
            self.driver.find_element(*TopVoluntariPage.buttonVoluntari).click()
            Voluntari.append(self.driver.find_elements(*TopVoluntariPage.voluntari))
        return Voluntari

    def getHarta(self):
        self.wait.until(expected_conditions.presence_of_element_located((TopVoluntariPage.harta)))
        return self.driver.find_element(*TopVoluntariPage.harta)

    def hartaZoomIn(self):
        time.sleep(1)
        if self.driver.find_element(*TopVoluntariPage.buttonZoomIn).is_enabled():
            return self.driver.find_element(*TopVoluntariPage.buttonZoomIn)

    def hartaZoomOut(self):
        time.sleep(1)
        if self.driver.find_element(*TopVoluntariPage.buttonZoomOut).is_enabled():
            return self.driver.find_element(*TopVoluntariPage.buttonZoomOut)




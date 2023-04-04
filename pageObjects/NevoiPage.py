import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class NevoiPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    nevoi = (By.XPATH, "//ul/li[2]/a/p")
    vizualizeaza = (By.XPATH, "//tr[1]//i[@title='Vizualizeaza']")
    aplica = (By.XPATH, "//i[2][not(contains(@disabled,'disabled'))]")
    confAplica = (By.XPATH, "//footer/button[1]")
    completeaza = (By.XPATH, "//tr[1]//i[3]")
    star = (By.CSS_SELECTOR, "span:nth-child(5) polygon:last-of-type")
    search = (By.NAME, "Filter")
    comment = (By.XPATH, "//div/textarea")

    def getNevoiPage(self):
        self.wait.until(expected_conditions.element_to_be_clickable((NevoiPage.nevoi)))
        self.wait.until(expected_conditions.presence_of_element_located((NevoiPage.nevoi)))
        return self.driver.find_element(*NevoiPage.nevoi)

    def getVizualizeaza(self):
        self.wait.until(expected_conditions.element_to_be_clickable((NevoiPage.vizualizeaza)))
        self.wait.until(expected_conditions.presence_of_element_located((NevoiPage.vizualizeaza)))
        return self.driver.find_element(*NevoiPage.vizualizeaza)

    def getAplica(self):
        self.wait.until(expected_conditions.element_to_be_clickable((NevoiPage.aplica)))
        self.wait.until(expected_conditions.presence_of_element_located((NevoiPage.aplica)))
        return self.driver.find_element(*NevoiPage.aplica)

    def getConfirmaAplicarea(self):
        self.wait.until(expected_conditions.element_to_be_clickable((NevoiPage.confAplica)))
        self.wait.until(expected_conditions.presence_of_element_located((NevoiPage.confAplica)))
        return self.driver.find_element(*NevoiPage.confAplica)

    def getCompleteaza(self):
        self.wait.until(expected_conditions.element_to_be_clickable((NevoiPage.completeaza)))
        self.wait.until(expected_conditions.presence_of_element_located((NevoiPage.completeaza)))
        return self.driver.find_element(*NevoiPage.completeaza)

    def getStar(self):
        self.wait.until(expected_conditions.element_to_be_clickable((NevoiPage.star)))
        self.wait.until(expected_conditions.presence_of_element_located((NevoiPage.star)))
        return self.driver.find_element(*NevoiPage.star)

    def getSearch(self):
        self.driver.find_element(*NevoiPage.search).clear()
        return self.driver.find_element(*NevoiPage.search)

    def getComment(self):
        return self.driver.find_element(*NevoiPage.comment)
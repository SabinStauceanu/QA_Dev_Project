import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class NevoiRecomandatePage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    nevoi = (By.XPATH, "//ul/li[3]/a/p")
    addBtn = (By.CSS_SELECTOR, "button[type='submit']")
    nume = (By.NAME, "contact_first_name")
    prenume = (By.NAME, "contact_last_name")
    nrTel = (By.NAME, "contact_phone_number")
    cat = (By.CSS_SELECTOR, "div[role='combobox']")
    catList = (By.XPATH, "//ul[@role='listbox']/li")
    descriere = (By.NAME, "description")
    strada = (By.XPATH, "//div[4]//input")
    detalii = (By.NAME, "details")
    judet = (By.NAME, "county")
    oras = (By.NAME, "city")
    zip = (By.NAME, "postal_code")
    send = (By.CSS_SELECTOR, ".btn.btn-primary")
    eroare = (By.XPATH, "//div[@role='group']/div/div/span")
    vizualizeaza = (By.XPATH, "//tr[1]//i[@title='Vizualizeaza']")
    sterge = (By.XPATH, "//tr[1]//i[@title='Sterge']")
    confSetrge = (By.XPATH, "//footer/button[1]")
    search = (By.NAME, "Filter")

    def getNevoiRecomandatePage(self):
        self.wait.until(expected_conditions.element_to_be_clickable((NevoiRecomandatePage.nevoi)))
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.nevoi)))
        return self.driver.find_element(*NevoiRecomandatePage.nevoi)

    def getAdaugareNevoi(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.addBtn)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.addBtn)))
        return self.driver.find_element(*NevoiRecomandatePage.addBtn)

    def getNume(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.nume)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.nume)))
        return self.driver.find_element(*NevoiRecomandatePage.nume)

    def getPrenume(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.prenume)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.prenume)))
        return self.driver.find_element(*NevoiRecomandatePage.prenume)

    def getNrTel(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.nrTel)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.nrTel)))
        return self.driver.find_element(*NevoiRecomandatePage.nrTel)

    def getCategorie(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.cat)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.cat)))
        self.driver.find_element(*NevoiRecomandatePage.cat).click()
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.catList)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.catList)))
        return self.driver.find_elements(*NevoiRecomandatePage.catList)

    def getDescriere(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.descriere)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.descriere)))
        return self.driver.find_element(*NevoiRecomandatePage.descriere)

    def getStrada(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.strada)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.strada)))
        return self.driver.find_element(*NevoiRecomandatePage.strada)

    def getDetalii(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.detalii)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.detalii)))
        return self.driver.find_element(*NevoiRecomandatePage.detalii)

    def getJudet(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.judet)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.judet)))
        return self.driver.find_element(*NevoiRecomandatePage.judet)

    def getOras(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.oras)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.oras)))
        return self.driver.find_element(*NevoiRecomandatePage.oras)

    def getCodPostal(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.zip)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.zip)))
        return self.driver.find_element(*NevoiRecomandatePage.zip)

    def getTrimite(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.send)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.send)))
        return self.driver.find_element(*NevoiRecomandatePage.send)

    def getMesajEroare(self):
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.eroare)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.eroare)))
        return self.driver.find_element(*NevoiRecomandatePage.eroare)

    def getVizualizeaza(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.vizualizeaza)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.vizualizeaza)))
        return self.driver.find_element(*NevoiRecomandatePage.vizualizeaza)

    def getSterge(self):
        self.wait.until(expected_conditions.presence_of_element_located((NevoiRecomandatePage.sterge)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.sterge)))
        return self.driver.find_element(*NevoiRecomandatePage.sterge)

    def getConfirmareStergere(self):
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.confSetrge)))
        self.wait.until(expected_conditions.visibility_of_element_located((NevoiRecomandatePage.confSetrge)))
        return self.driver.find_element(*NevoiRecomandatePage.confSetrge)

    def getSearch(self):
        self.driver.find_element(*NevoiRecomandatePage.search).clear()
        return self.driver.find_element(*NevoiRecomandatePage.search)



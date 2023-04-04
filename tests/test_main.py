import time

from pageObjects.Autentificare import Autentificare
from pageObjects.Headers import Headers
from pageObjects.NevoiPage import NevoiPage
from pageObjects.NevoiRecomandatePage import NevoiRecomandatePage
from pageObjects.TopVoluntariPage import TopVoluntariPage
from utilities.BaseClass import BaseClass


class TestDevQA(BaseClass):
    def test_TC1(self):
        log = self.getLogger()
        headers = Headers(self.driver, self.wait)
        headers.getTopVoluntari().click()
        headers.getListaNevoi().click()
        headers.getDespreNoi().click()
        headers.getOfertaSugestie().click()
        headers.getDevinoVoluntar().click()
        headers.getAutentificare().click()
        headers.getAcasa().click()
        log.info("TC1 has Passed!")

    def test_TC2(self):
        log = self.getLogger()
        headers = Headers(self.driver, self.wait)
        topVoluntari = TopVoluntariPage(self.driver, self.wait)
        headers.getTopVoluntari().click()
        assert topVoluntari.getHarta().is_displayed()
        voluntari = topVoluntari.getVoluntari()
        log.info("The number of volunteer registered is:" + str(len(voluntari)))
        log.info("TC2 has passed!")

    def test_TC3(self):
        log = self.getLogger()
        topVoluntari = TopVoluntariPage(self.driver, self.wait)
        topVoluntari.hartaZoomIn().click()
        topVoluntari.hartaZoomOut().click()
        log.info("TC3 has passed!")

    def test_TC4(self):
        log = self.getLogger()
        autentificare = Autentificare(self.driver, self.wait)
        headers = Headers(self.driver, self.wait)
        headers.getAutentificare().click()
        autentificare.getTel().send_keys("0756671715")
        autentificare.getPass().send_keys("sabin500")
        autentificare.getAuth().click()
        log.info("TC4 has passed!")

    def test_TC5(self):
        log = self.getLogger()
        autentificare = Autentificare(self.driver, self.wait)
        headers = Headers(self.driver, self.wait)
        autentificare.getDisconnect().click()
        headers.getAutentificare().click()
        autentificare.getTel().send_keys("080080080")
        autentificare.getPass().send_keys("gregory")
        autentificare.getAuth().click()
        log.info("Mesajul de eroare este:" + autentificare.getEroare().text)
        log.info("TC5 has passed!")

    def test_TC6(self):
        log = self.getLogger()
        autentificare = Autentificare(self.driver, self.wait)
        nevoiRecomandatePage = NevoiRecomandatePage(self.driver, self.wait)
        autentificare.getTel().send_keys("0756671715")
        autentificare.getPass().send_keys("sabin500")
        autentificare.getAuth().click()
        nevoiRecomandatePage.getNevoiRecomandatePage().click()
        nevoiRecomandatePage.getAdaugareNevoi().click()
        nevoiRecomandatePage.getNume().send_keys("Rick")
        nevoiRecomandatePage.getPrenume().send_keys("Morty")
        nevoiRecomandatePage.getNrTel().send_keys("080080080")
        categorie = nevoiRecomandatePage.getCategorie()
        try:
            for categoria in categorie:
                if categoria.text == "Alimente":
                    categoria.click()
        finally:
            nevoiRecomandatePage.getDescriere().send_keys("I am hangry")
            nevoiRecomandatePage.getStrada().send_keys("Wall Street, number 89")
            nevoiRecomandatePage.getDetalii().send_keys("floor 100, apartment 404")
            nevoiRecomandatePage.getJudet().send_keys("New York")
            nevoiRecomandatePage.getOras().send_keys("Alaska")
            nevoiRecomandatePage.getCodPostal().send_keys("717101")
            nevoiRecomandatePage.getTrimite().click()
            nevoiRecomandatePage.getNevoiRecomandatePage().click()
            log.info("TC6 has passed!")

    def test_TC7(self):
        log = self.getLogger()
        nevoiRecomandatePage = NevoiRecomandatePage(self.driver, self.wait)
        nevoiRecomandatePage.getAdaugareNevoi().click()
        nevoiRecomandatePage.getNume().send_keys("John")
        nevoiRecomandatePage.getPrenume().send_keys("Cena")
        nevoiRecomandatePage.getNrTel().send_keys("080080081")
        categorie = nevoiRecomandatePage.getCategorie()
        for categoria in categorie:
            if categoria.text == "Medicamente":
                categoria.click()
        nevoiRecomandatePage.getStrada().send_keys("Miami Beach, number 77")
        nevoiRecomandatePage.getDetalii().send_keys("floor 0, apartment 2")
        nevoiRecomandatePage.getJudet().send_keys("California")
        nevoiRecomandatePage.getOras().send_keys("Canada")
        nevoiRecomandatePage.getCodPostal().send_keys("717100")
        nevoiRecomandatePage.getTrimite().click()
        log.info("Mesajul de eroare este:" + nevoiRecomandatePage.getMesajEroare().text)
        nevoiRecomandatePage.getNevoiRecomandatePage().click()
        log.info("TC7 has passed!")

    def test_TC8(self):
        log = self.getLogger()
        nevoiRecomandatePage = NevoiRecomandatePage(self.driver, self.wait)
        nevoiRecomandatePage.getVizualizeaza().click()
        nevoiRecomandatePage.getNevoiRecomandatePage().click()
        log.info("TC8 has passed!")

    def test_TC9(self):
        log = self.getLogger()
        nevoiRecomandatePage = NevoiRecomandatePage(self.driver, self.wait)
        nevoiRecomandatePage.getClickStatus().click()
        nevoiRecomandatePage.getClickStatus().click()
        nevoiRecomandatePage.getSterge().click()
        nevoiRecomandatePage.getConfirmareStergere().click()
        log.info("TC9 has passed!")

    def test_TC10(self):
        log = self.getLogger()
        nevoiRecomandatePage = NevoiRecomandatePage(self.driver, self.wait)
        nevoiRecomandatePage.getSearch().send_keys("I am hangry")
        nevoiRecomandatePage.getSearch().send_keys("Rick")
        nevoiRecomandatePage.getSearch().send_keys("Wall")
        nevoiRecomandatePage.getSearch().send_keys("080080080")
        log.info("TC10 has passed!")

    def test_TC11(self):
        log = self.getLogger()
        nevoiPage = NevoiPage(self.driver, self.wait)
        nevoiPage.getNevoiPage().click()
        nevoiPage.getVizualizeaza().click()
        log.info("TC11 has passed!")

    def test_TC12(self):
        log = self.getLogger()
        nevoiPage = NevoiPage(self.driver, self.wait)
        nevoiPage.getNevoiPage().click()
        nevoiPage.getAplica().click()
        nevoiPage.getConfirmaAplicarea().click()
        log.info("TC12 has passed!")

    def test_TC13(self):
        log = self.getLogger()
        nevoiPage = NevoiPage(self.driver, self.wait)
        nevoiPage.getSearch().send_keys("In")
        nevoiPage.getCompleteaza().click()
        nevoiPage.getStar().click()
        nevoiPage.getComment().send_keys("Salut, sunt Stauceanu Sabin, NR. 1 voluntar :).")
        nevoiPage.getConfirmaAplicarea()
        log.info("TC13 has passed!")

    def test_TC14(self):
        log = self.getLogger()
        autentificare = Autentificare(self.driver, self.wait)
        autentificare.getClosePopup().click()
        autentificare.getDisconnect().click()
        log.info("TC14 has passed!")



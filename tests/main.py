import time

import requests

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
        log.info("The number of volunteer present on page is:" + str(len(voluntari)))
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
        # Am folosit try finally deoarece imi da eroare la linia 79 si totusi linia respectiva se executa urmand sa imi opreasca procesul de a rula codul dupa linia respectiva
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

    def test_TC15(self):
        log = self.getLogger()
        ENDPOINT = 'https://iwanttohelp.bim.assistcloud.services/volunteers/api/v1/profile'
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
                   'authority':'iwanttohelp.bim.assistcloud.services',
                   'accept':'application/json',
                   'accept-language':'en-US,en;q=0.9',
                   'access-control-allow-origin':'*',
                   'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODE4MDMyNjAsInN1YiI6N30.qyuWZe_euBogn-MdgDRN8YqHw8NIJw7a2_35dkx3OPk',
                   'referer':'https://iwanttohelp.bim.assistcloud.services/dashboard/profile',
                   'sec-ch-ua':'"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                   'sec-ch-ua-mobile':'?0',
                   'sec-ch-ua-platform':'Windows',
                   'sec-fetch-mode':'cors',
                   'sec-fetch-dest':'empty',
                   'sec-fetch-site':'cors', }

        response = requests.get(ENDPOINT, headers=headers)
        log.info(response.status_code)
        log.info(response.json())
        log.info("TC15 has passed!")

    def test_TC16(self):
        log = self.getLogger()
        ENDPOINT = 'https://iwanttohelp.bim.assistcloud.services/volunteers/api/v1/recommended_needs'
        headers = {'authority':'iwanttohelp.bim.assistcloud.services:accept:application/json',
                    'accept-language':'en-US,en;q=0.9',
                    'access-control-allow-origin':'*',
                    'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODE4MDMyNjAsInN1YiI6N30.qyuWZe_euBogn-MdgDRN8YqHw8NIJw7a2_35dkx3OPk',
                    'if-none-match':'W/"f683fbe4a26024b616d68d264dd05c9a"',
                    'referer':'https://iwanttohelp.bim.assistcloud.services/dashboard/recommended_needs',
                    'sec-ch-ua':'"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                    'sec-ch-ua-mobile':'?0',
                    'sec-ch-ua-platform':'"Windows"',
                    'sec-fetch-dest':'empty',
                    'sec-fetch-mode':'cors',
                    'sec-fetch-site':'same-origin',
                    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        response = requests.get(ENDPOINT, headers=headers)
        log.info(response.status_code)
        log.info(response.json())
        log.info("TC16 has passed!")


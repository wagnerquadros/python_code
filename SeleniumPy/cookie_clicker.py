from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class CookieCliecker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons": {
                "cookie": {
                    "id": "bigCookie"
                },
                "upgrade": {
                    "id": "product$$NUMBER$$"
                },
                "idioma": {
                    "xpath": "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[10]"
                }
            }
        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["idioma"]["xpath"]).click()
        time.sleep(10)

    def clicar_no_cookie(self):
        self.driver.find_element(By.ID, self.SITE_MAP["buttons"]["cookie"]["id"]).click()

    def pega_melhor_upgrade(self):
        encontrei = False
        elemento_atual = 1

        while not encontrei:
            objeto = self.driver.find_element(By.ID, self.SITE_MAP["buttons"]["upgrade"]["id"].replace("$$NUMBER$$", str(elemento_atual)))
            classes_objeto = objeto.get_attribute("class")

            if not "enabled" in classes_objeto:
                encontrei = True
            else:
                elemento_atual +=1
        return elemento_atual-1

    def comprar_upgrade(self):
        objeto = self.driver.find_element(By.ID, self.SITE_MAP["buttons"]["upgrade"]["id"].replace("$$NUMBER$$", str(self.pega_melhor_upgrade())))
        objeto.click()



biscoito = CookieCliecker()
biscoito.abrir_site()

i = 0

while True:
    if i % 500 == 0 and i != 0:
        time.sleep(1)
        biscoito.comprar_upgrade()
        time.sleep(1)
    biscoito.clicar_no_cookie()
    i += 1
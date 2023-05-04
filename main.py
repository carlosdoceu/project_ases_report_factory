import numpy as np
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime
import create_table_matriz
from create_table_matriz import createTableEmpty

options = webdriver.ChromeOptions()
options.headless = False
navegador = webdriver.Chrome(chrome_options=options)

tabelasProntas = []
tabelaUnica = create_table_matriz.createTableEmpty(create_table_matriz.matriz)

# este vetor ira conter todos as paginas na qual servira para o relatorio
urls = ['https://www.google.com/', 'www.tjro.jus.br']


def abreNavegador():
    navegador.get("https://asesweb.governoeletronico.gov.br")
    navegador.find_element(By.ID, 'url').clear()
    navegador.find_element(By.ID, 'url').send_keys(url)
    navegador.find_element(By.XPATH, '//*[@id="input_tab_1"]').click()


# for vai iniciar navegacao e identifica xpath e insere em vetores
for i, url in enumerate(urls):
    print(f"Analisando Páginas  {i + 1}/{len(urls)}: {url}")
    abreNavegador()
    # time.sleep(5)

    rows = len(navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tbody/tr'))
    cols = len(
        navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tbody/tr[1]/td'))

    veterros = []
    vetavisos = []
    resultTab = []
    for i in range(1, rows + 1):

        for j in range(1, cols + 1):
            element = navegador.find_element(By.XPATH,
                                             "//*[@id='tabelaErros']/tbody/tr[" + str(i) + "]/td[" + str(j) + "]")
            if j == 2:
                veterros.append(element.text)
            elif j == 3:
                vetavisos.append(element.text)
    # resultTab.append({"erros": veterros, "avisos": vetavisos})

            tabelaUnica[1][8] = navegador.find_element(By.XPATH, "//*[@id='total']/td[2]").text
            tabelaUnica[2][8] = navegador.find_element(By.XPATH, "//*[@id='total']/td[3]").text
            tabelaUnica[1][9] = navegador.find_element(By.XPATH, "//*[@id='webaxscore']/span").text
            tabelaUnica[1][10] = datetime.now().strftime("%H:%M:%S %d/%m/%Y")

    tabelasProntas.append(tabelaUnica)





    print(resultTab)


    # tabelasProntas.append(resultTab)


for i in veterros:
    print("erros:", i)
for j in vetavisos:
    print("avisos:", j)

for i,tabela in enumerate(tabelasProntas):
    print(f"Tabela {i+1}:")
    print(pd.DataFrame(tabela))
tabelaCompleta = pd.concat(tabelasProntas, axis=0)
tabelaCompleta.to_csv("relatorio.csv")
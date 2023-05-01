
import numpy as np
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import csv

import create_table_matriz
from create_table_matriz import createTableEmpty

options = webdriver.ChromeOptions()
options.headless = False
navegador = webdriver.Chrome(chrome_options=options)


matrizvazia = create_table_matriz.createTableEmpty(create_table_matriz.matriz)
df = pd.DataFrame(createTableEmpty(matrizvazia))
df.to_csv("testedematriz.csv", index=False, header=False)

# este vetor ira conter todos as paginas na qual servira para o relatorio
urls = ['https://www.tjro.jus.br/', 'https://www.tjro.jus.br/resp-institucional/resp-conheca-pj','https://www.tjro.jus.br/resp-institucional/resp-legislacao-normas#?pparentid=1&menuType=legislacao-e-normas',"https://www.tjro.jus.br/resp-institucional/resp-cons-magistratura"]

templist = []

# for vai realizar navega e identifica tags
for i, url in enumerate(urls):
    print(f"Processando URL {i + 1}/{len(urls)}: {url}")
    navegador.get("https://asesweb.governoeletronico.gov.br")
    navegador.find_element(By.ID, 'url').clear()
    navegador.find_element(By.ID, 'url').send_keys(url)
    navegador.find_element(By.XPATH, '//*[@id="input_tab_1"]').click()
    # time.sleep(5)

    rows = len(navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tbody/tr'))
    cols = len(
        navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tbody/tr[1]/td'))

    row_total = len(
        navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tfoot/tr'))
    cols_total = len(
        navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tfoot/tr/td'))

    percentage = len(
        navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[1]/div/div/span'))

    resultTab = []
    for i in range(1, rows + 1):
        d = []
        for j in range(1, cols + 1):
            d.append(navegador.find_element(By.XPATH,"//*[@id='tabelaErros']/tbody/tr[" + str(i) + "]/td[" + str(j) + "]").text)
        resultTab.append({"secao": d[0], "erros": d[1], "avisos": d[2]})
    print(resultTab)
    templist.append(resultTab)


# dfMatriz= pd.DataFrame(matrizVazia)

df =pd.DataFrame(templist)

# dfMatriz.to_csv("matrizVazia", index=False, header=False)
df.to_csv("tabela.csv", index=False)

print("Terminouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu!")

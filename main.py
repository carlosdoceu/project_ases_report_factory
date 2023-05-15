from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import create_table_matriz
from create_table_matriz import createTableEmpty

options = webdriver.ChromeOptions()
options.headless = False
navegador = webdriver.Chrome(chrome_options=options)


tabelaUnica = create_table_matriz.createTableEmpty(create_table_matriz.matriz)
todasTabelas=[]
# este vetor ira conter todos as paginas na qual servira para o relatorio
urls = ['https://www.google.com/','https://www.tjro.jus.br/','https://www.tjro.jus.br/resp-institucional/resp-conheca-pj']
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
    cols = len(navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tbody/tr[1]/td'))
    veterros = []
    vetavisos = []
    resultTab = []
    tabelaUnica = create_table_matriz.createTableEmpty(create_table_matriz.matriz)


    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            element = navegador.find_element(By.XPATH,"//*[@id='tabelaErros']/tbody/tr[" + str(i) + "]/td[" + str(j) + "]")
            if j == 2:
                veterros.append(element.text)
            elif j == 3:
                vetavisos.append(element.text)

            # Coleta conteudo adicional
            script = "return document.evaluate(\"//*[@id='content']/div[3]\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.textContent;"
            texto_extraido = navegador.execute_script(script)

            inicio_titulo = texto_extraido.find("Título: ") + len("Título: ")
            inicio_link = texto_extraido.find("Página: ") + len("Página: ")

            fim_titulo = texto_extraido.find("\n", inicio_titulo)
            fim_link = texto_extraido.find("\n", inicio_link)

            tabelaUnica[0][0] = texto_extraido[inicio_titulo:fim_titulo].strip()
            tabelaUnica[0][1] = texto_extraido[inicio_link:fim_link].strip()
            # total Erros
            tabelaUnica[1][8] = navegador.find_element(By.XPATH, "//*[@id='total']/td[2]").text
            # total Avisos
            tabelaUnica[2][8] = navegador.find_element(By.XPATH, "//*[@id='total']/td[3]").text
            # porcentagem
            tabelaUnica[1][9] = navegador.find_element(By.XPATH, "//*[@id='webaxscore']/span").text
            # apuração
            tabelaUnica[1][10] = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    #fim da coleta
    #adiciona valores "ERROS" e "AVISOS" nas tabelas
    for i in range(len(veterros)):
        tabelaUnica[1][i + 2] = veterros[i]
    for i in range(len(vetavisos)):
        tabelaUnica[2][i + 2] = vetavisos[i]

    tabelaUnica_df = pd.DataFrame(tabelaUnica)
    todasTabelas.append(tabelaUnica_df)
    #separador para ficar mais organizado
    separador = pd.DataFrame([[''] * len(tabelaUnica_df.columns)], columns=tabelaUnica_df.columns)
    todasTabelas.append(separador)

tabelaFinal = pd.concat(todasTabelas, ignore_index=True).reset_index(drop=True)
is_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"relatorio_{is_now}.csv"
tabelaFinal.to_csv(file_name, index=False,header=False)

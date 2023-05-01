import pandas as pd
import numpy as np
from datetime import datetime

#######################################################
### Vai celulas vazias para popular depois ###
#######################################################

# Define os vetores colunas e linhas
colunas = ['link', 'apuracao', 'porcentagem', 'marcacao', 'comportamento', 'conteudo_informacao', 'apresentacao_design',
           'multimidia', 'formulario', 'total']
linhas = ['erros', 'avisos']

# Junta vetores e cria matriz
matriz = np.zeros((len(linhas) + 1, len(colunas)), dtype=object)


# cria tabela base vazia para criar ser populada
def createTableEmpty(matriz):
    for i in range(len(linhas)):
        matriz[i + 1, 0] = linhas[i]
        for j in range(len(colunas)):
            matriz[0, j] = colunas[j]
    return matriz





df = pd.DataFrame(createTableEmpty(matriz))

# Define um dicionário com os estilos
styles = [
    dict(selector="th", props=[("font-size", "14pt"), ("background-color", "gray"), ("color", "white")]), # cabeçalho
    dict(selector="td", props=[("font-size", "12pt")]), # células
]

# Aplica os estilos à tabela
styled_table = df.style.set_table_styles(styles)





is_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"relatorio_{is_now}.csv"

df.to_csv(file_name, index=False, header=False)

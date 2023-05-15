import pandas as pd
import numpy as np
from datetime import datetime



colunas = ['titulo', 'link', 'marcação', 'comportamento', 'conteudo_informação', 'apresentacao_design',
           'multimidia', 'formulario', 'total', 'porcentagem', 'apuração']
linhas = ['erros', 'avisos']

matriz = np.zeros((len(linhas) + 1, len(colunas)), dtype=object)

def createTableEmpty(matriz):
    for i in range(len(linhas)):
        matriz[i + 1, 0] = linhas[i]
        for j in range(len(colunas)):
            matriz[0, j] = colunas[j]
    return matriz

matriz = createTableEmpty(matriz)
# #
# for j in range(2, 8):
#     matriz[1, j] = 1
#
# for j in range(2, 8):
#     matriz[2, j] = 2
#
#
#
#
# #dado preenchido
# matriz[0][0]="banana"
#
#
#
#
#
# df = pd.DataFrame(matriz)
#
# is_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# file_name = f"relatorio_{is_now}.csv"
#
# df.to_csv(file_name, index=False, header=False, encoding='utf-8')

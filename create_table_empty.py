import numpy as np
import pandas as pd
from datetime import datetime

#######################################################
### Vai celulas vazias para popular depois ###
#######################################################

# Define as colunas e linhas para armazenamento posterior
colunas = ['link', 'apuracao', 'porcentagem', 'marcacao', 'comportamento', 'conteudo_informacao', 'apresentacao_design',
           'multimidia', 'formulario', 'total']
linhas = ['erros', 'avisos']

# Cria um DataFrame com células vazias (preenchidas com NaN)
dados = pd.DataFrame(np.nan, index=linhas, columns=colunas)


today=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"relatorio_{today}.csv"
dados.to_csv(file_name, index=False)
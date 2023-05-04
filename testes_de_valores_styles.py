import pandas as pd

# Cria um dataframe com as colunas A e B
df1 = pd.DataFrame({'A': ['valor A1'], 'B': ['valor B1']})

# Cria um dataframe com as colunas B e C
df2 = pd.DataFrame({'B': ['valor B1'], 'C': ['valor C1']})

# Mescla os dois dataframes usando a coluna B como chave de mesclagem
df3 = pd.merge(df1, df2, on='B')

# Imprime o resultado da mesclagem
print(df3)

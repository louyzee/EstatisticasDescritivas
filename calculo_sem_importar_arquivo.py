import pandas as pd
import numpy as np

#data = pd.read_csv('salarios.csv')

# dataframe = pd.DataFrame()
# series = pd.Series()
# serie = pd.Series(dados_df['Peso'])
# dataframe.describe() - mostra estatísticas descritivas
dados = {'Nome': ['Otavio', 'Sandra', 'Ana', 'Francisco'],
         'NotaAluno': [1, 2, 2, 3],
         'Sexo': ['Masculino', 'Feminino', 'Feminino', 'Masculino'],
         'Idade': [18, 19, 18, 22],
         'Peso': [98, 66, 102, 76],
         'Altura': [1.780, 1.680, 1.570, 1.590]
        }

dados_df = pd.DataFrame(dados)
dadosNum = { 
    'NotaAluno': dados_df.NotaAluno,
    'Idade': dados_df.Idade,
    'Peso': dados_df.Peso,
    'Altura': dados_df.Altura
}
dadosNum_df = pd.DataFrame(dadosNum)

# Média
media = dados_df.mean()
print('Média: ')
print(media,'\n')


# Mediana
mediana = dados_df.median()
print('Mediana: ')
print(mediana,'\n')


# Moda
moda = dados_df.mode()
print('Moda: ')
print(moda,'\n')

# Quartil
quartil = dados_df.quantile()
print('Quartil: ')
print(quartil,'\n')


# Variância
variancia = dados_df.var()
print('Variância: ')
print(variancia,'\n')

# Desvio Padão
desvio = dados_df.std()
print('Desvio Padrão: ')
print(desvio,'\n')

print('Outros dados:')
print(dados_df.describe())

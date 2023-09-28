import pandas as pd

# dataframe = pd.DataFrame()
# series = pd.Series()
# dataframe.describe() - mostra estatísticas descritivas

dados = {'Nome': ['Otavio', 'Sandra', 'Ana', 'Francisco', 'Rafael'],
         'NotaDoAluno': [1, 2, 2, 3, 3],
         'Sexo': ['Masculino', 'Feminino', 'Feminino', 'Masculino', 'Masculino'],
         'Idade': [18, 19, 18, 22, 18],
         'Peso': [98, 66, 102, 76, 90],
         'Altura': [1.780, 1.680, 1.570, 1.590, 1.630]
        }

dados_df = pd.DataFrame(dados)
dadosNum = { 
    'NotaAluno': dados_df.NotaAluno,
    'Idade': dados_df.Idade,
    'Peso': dados_df.Peso,
    'Altura': dados_df.Altura
}
dadosNum_df = pd.DataFrame(dadosNum)

#Exibição dos dados a serem utilizados
print('Dados utilizados:')
print(dados_df,'\n')

# Média
media = dadosNum_df.mean()
print('Média: ')
print(media,'\n')

# Mediana
mediana = dadosNum_df.median()
print('Mediana: ')
print(mediana,'\n')

# Moda
moda = dados_df.drop(['Nome'],axis=1).mode()
print('Moda: ')
print(moda,'\n')

# Quartil
quartil = dadosNum_df.quantile()
print('Quartil: ')
print(quartil,'\n')

# Variância
variancia = dadosNum_df.var()
print('Variância: ')
print(variancia,'\n')

# Desvio Padão
desvio = dadosNum_df.std()
print('Desvio Padrão: ')
print(desvio,'\n')

print('Outros dados:')
print(dados_df.describe(),'\n')

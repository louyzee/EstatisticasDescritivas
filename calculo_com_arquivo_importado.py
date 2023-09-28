import pandas as pd

# dataframe = pd.DataFrame()
# series = pd.Series()
# dataframe.describe() - mostra estatísticas descritivas

dados = pd.read_csv('dados_pessoas_e_notas.csv')

dados_df = pd.DataFrame(dados)
dadosNum = { 
    'NotaDoAluno': dados_df.NotaDoAluno,
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

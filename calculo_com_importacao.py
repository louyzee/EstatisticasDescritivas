import pandas as pd

# dataframe = pd.DataFrame()
# series = pd.Series()
# dataframe.describe() - mostra estatísticas descritivas

#dados = pd.read_csv('dados_pessoas_e_notas.csv')
dados = pd.read_csv("https://raw.githubusercontent.com/ect-info/ml/master/dados/didatico_dados_pessoas_e_notas.csv")

dados_df = pd.DataFrame(dados)
dadosNum = { 
    'Nota do aluno': dados_df['Nota do aluno'],
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

# Moda
moda = dados_df.drop(['Nome'],axis=1).mode()
print('Moda: ')
print(moda,'\n')

# Mediana
mediana = dadosNum_df.median()
print('Mediana: ')
print(mediana,'\n')

# Quartil
print('1º Quartil: ')
print(dadosNum_df.quantile(q=0.25),'\n')

print('2º Quartil: ')
print(dadosNum_df.quantile(q=0.50),'\n')

print('3º Quartil: ')
print(dadosNum_df.quantile(q=0.75),'\n')

# Variância
variancia = dadosNum_df.var()
print('Variância: ')
print(variancia,'\n')

# Desvio Padão
desvio = dadosNum_df.std()
print('Desvio Padrão: ')
print(desvio,'\n')

#Amplitudes
print('Amplitude máxima: ')
print(dadosNum_df.max(),'\n')

print('Amplitude mínima: ')
print(dadosNum_df.min(),'\n')

print('Amplitude: ')
print(dadosNum_df.max() - dadosNum_df.min(),'\n')


print('Alguns dados agrupados:')
print(dados_df.describe(),'\n')

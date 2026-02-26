import pandas as pd;

import matplotlib.pyplot as plt;

import seaborn as sns;

url = 'https://raw.githubusercontent.com/alura-cursos/estatistica-r-frequencias-medidas/refs/heads/main/dados/vendas_ecommerce.csv '

#####################################################################################################################

df = pd.read_csv(url)

df['categoria_produto'].unique()

df['categoria_produto'].value_counts()

produtos = df['categoria_produto'].value_counts().reset_index()


plt.barh(produtos['categoria_produto'], produtos['count'])

plt.show()

####################################################################################################################

sorted(df['avaliacao'].unique())


df['avaliacao indicador'] = pd.Categorical(
    df['avaliacao'],
    categories=[1, 2, 3, 4, 5],
    ordered=True
  )

avaliacao_labels = {1: 'Péssimo', 2: 'Ruim', 3: 'Regular', 4: 'Bom', 5: 'Ótimo'}
df['avaliacao indicador'] = df['avaliacao indicador'].map(avaliacao_labels)

df_unico = df[['avaliacao', 'avaliacao indicador']].drop_duplicates()

df['quantidade'].unique()

df['total_compra'].unique()

print(f"Tivemos vendas a partir de R$ {min(df['total_compra']):,.2f} até R$ {max(df['total_compra']):,.2f}")

df.sort_values(by='total_compra')

freq_avaliacoes = (df.groupby('avaliacao indicador', observed=False)
                   .size()
                   .reset_index(name='freq_absoluta')
                   .sort_values(by='avaliacao indicador', ascending=False))

freq_avaliacoes['freq_relativa'] = round((freq_avaliacoes['freq_absoluta'] / freq_avaliacoes['freq_absoluta'].sum()) * 100, 1)

freq_avaliacoes.columns = ['Avaliação', 'Quantidade', 'Porcentagem (%)']

plt.figure(figsize=(10, 6))
sns.barplot(data=freq_avaliacoes, x='Avaliação', y='Quantidade')

# Adicionando título e rótulos aos eixos
plt.title("Distribuição de Frequências das Avaliações")
plt.xlabel("Avaliação")
plt.ylabel("Frequência")


# Adicionando os rótulos com valores de frequência e porcentagem
for index, row in freq_avaliacoes.iterrows():
    plt.text(index, row['Quantidade'] + 0.1, f"{row['Quantidade']} ({row['Porcentagem (%)']:.1f}%)",
             ha='center', va='bottom', fontsize=12)


plt.show()

##########################################################################################

tab_avaliacoes_regiao = pd.crosstab(df['avaliacao indicador'], df['regiao_cliente'])

tab_avaliacoes_regiao_relativa = pd.crosstab(df['avaliacao indicador'], df['regiao_cliente'], normalize = 'columns') * 100

tab_avaliacoes_regiao_relativa = round(tab_avaliacoes_regiao_relativa, 1)

tab_avaliacoes_filtrada = tab_avaliacoes_regiao_relativa[tab_avaliacoes_regiao_relativa.index.isin(['Ótimo', 'Bom'])]

resultado = tab_avaliacoes_filtrada.sum()

tab_avaliacoes_filtrada = tab_avaliacoes_regiao_relativa[tab_avaliacoes_regiao_relativa.index.isin(['Ruim', 'Péssimo'])]

resultado = tab_avaliacoes_filtrada.sum()

#########################################################################################

ticket_medio = round(pd.crosstab(df['sexo_biologico'], df['regiao_cliente'], values=df['total_compra'], aggfunc='mean'), 2)

#########################################################################################


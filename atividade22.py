import pandas as pd 

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

dados = pd.read_csv(url, sep = ";");

dados.head(); # traz as primeiras 5 colunas ou o numero que voce definir da base de dados

#print(dados.tail(20)); # traz as ultimas 5 colunas ou o numero que voce definir da base de dados

type(dados); # tipo DataFrame

#read_csv(): Essa função é usada para ler arquivos CSV (Comma Separated Values), que são arquivos de texto que contêm dados separados por vírgulas. É possível passar diversos parâmetros para personalizar a leitura do csv, como delimitador, cabeçalho, tipo de encoding, entre outros.
#
#read_excel(): Essa função é usada para ler arquivos do Excel (.xls ou .xlsx) e criar um DataFrame a partir dos dados.
#
#read_json(): Essa função é usada para ler arquivos JSON (JavaScript Object Notation), que são arquivos de texto que contêm dados em formato de objeto JavaScript.
#
#read_html(): Essa função é usada para ler tabelas HTML, que são estruturas de dados organizadas em formato de tabela em uma página da web.
#
#read_sql(): Essa função é usada para ler dados de um banco de dados relacional, como o MySQL, PostgreSQL e SQL Server. O Pandas é capaz de importar dados de diferentes formas, permitindo ajustar parâmetros como a consulta, o nome da tabela e o tipo de dados das colunas.

dados.shape; # traz o tamanho da base de dados em uma tupla (linhas,colunas)

dados.columns # traz uma lista com os nomes das colunas

#dados.info() # traz os tipos de dados em cada coluna


#print(round(dados['Valor'].mean(),1));

df_preco_tipo = round(dados.groupby('Tipo')['Valor'].mean().sort_values(),1);

#df_preco_tipo.plot(kind = 'barh', figsize=(14,10), color='green');

#print(df_preco_tipo);

#print(dados.Tipo.unique())

imoveis_comerciais = ['Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão', 'Galpão/Depósito/Armazém', 'Casa Comercial', 'Terreno Padrão','Loja Shopping/ Ct Comercial', 'Box/Garagem', 'Chácara', 'Loteamento/Condomínio', 'Sítio','Pousada/Chalé', 'Hotel', 'Indústria']

df = dados.query('@imoveis_comerciais not in Tipo');

df_preco_residencial = round(df.groupby('Tipo')['Valor'].mean().sort_values(),1);

suites = dados.query('Suites != 0')
#print(suites)

percentual = df.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo');

#print(percentual)

df_apto = dados.query('Tipo == "Apartamento"');

#print(df.isnull().sum()); #informa o valor de valores que sao null e nao null  como (0, 1) .sum() soma os valores null e informa quantos existem em cada coluna

df  = df.fillna(0); #substitui todo NaN pelo que for escolhido (neste caso 0)

#Remover os dados nulos: É possível remover as linhas ou colunas que possuem valores nulos utilizando o método dropna() . Esse método remove todas as linhas ou colunas que possuem pelo menos um valor nulo.
#
#Preencher os dados nulos: Utilizando o método fillna(), podemos preencher os valores nulos com um valor específico. Além disso, também é possível utilizar argumentos específicos do método fillna() como o method=”ffill” ou method=”bfill” para preencher os valores nulos com o valor anterior ou posterior, respectivamente.
#
#Interpolar os dados nulos: É possível utilizar o método interpolate() para preencher os valores nulos com valores interpolados, ou seja, valores calculados a partir dos valores vizinhos.

dfApto = dados.query('Valor == 0 | Condominio == 0'); # seleciona todas as linhas dentro da base de dados que possuam Valor = 0 ou Condominio = 0
remover = dfApto.index; # Gera uma lista com os indices do query anterior
df.drop(remover, axis=0, inplace=True); # remove todos os indices informados na lista, axis (eixo X = 0, eixo Y = 1), inplace especifica as auteracoes no data frame

df.Tipo.unique() # mostra todos os valores existentes na coluna Tipo

df.drop('Tipo', axis=1, inplace= True);

selecaoQuarto1 = df['Quartos'] == 1;
selecaoValor1 = df['Valor'] < 1200;
selecaoFinal = selecaoQuarto1 & selecaoValor1;
 
#print(df[selecaoFinal]);
selecao2 = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70);
#selecao2 = df.query('Quartos >= 2 & Valor < 3000 & Area > 70')

print(selecao2)

#df.to_csv('dados_apartamentos.csv', index=False, sep = ;) gera um arquivo atualizado como .csv index = False faz com que nao seja gerado um novo indice sep = separador do csv



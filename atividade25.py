import pandas as pd;
import matplotlib.pyplot as plt;
import sqlalchemy; 
from sqlalchemy import create_engine, MetaData, Table, inspect;

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/superstore_data.csv';
url2 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/superstore_data_ponto_virgula.csv'

dados_mercado = pd.read_csv(url);
dados_ponto_virgula = pd.read_csv(url2, sep = ";")

#print(dados_ponto_virgula.head())

dados_primeiras_linhas = pd.read_csv(url, nrows=5); #gera apenas as 5 primeiras linhas
dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])#mostra apenas as colunas selecionadas
salvar = dados_selecao.to_csv('clientes_mercado.csv');


url3 = 'emissoes_CO2.xlsx'

dados_excel = pd.read_excel(url3);
pd.ExcelFile(url3).sheet_names;
#fontes = pd.read_excel(url, sheet_name='fontes')
#print(dados_excel.head());
intervalo = pd.read_excel(url3, sheet_name='emissoes_C02', usecols= 'A:D', nrows=10)
salvar2 = intervalo.to_excel('Planilha_reduzida.xlsx', index = False)
salvar2;


url4 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/pacientes.json';
url5 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/pacientes_2.json';
dados_json = pd.read_json(url4);
dados_json2 = pd.read_json(url5)
df_normalizado = pd.json_normalize(dados_json2['Pacientes']); #organiza e padroniza os dados
salvar3 = df_normalizado.to_json('dados_normalizados.json')

url6 = "AFI's 100 Years...100 Movies - Wikipedia.html"

dadosHTML = pd.read_html(url6)
lista2HTML = dadosHTML[1]

salvar3 =lista2HTML.to_html('segunda lista.html')
salvar3

url7 = 'imdb_top_1000.xml'
dadosXML = pd.read_xml(url7);

#print(dadosXML.head())
salva4 = dadosXML.to_xml('filmesimdb2')

engine = create_engine('sqlite:///:memory:')

url8 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/clientes_banco.csv'

dadosBanco = pd.read_csv(url8);

#print(dadosBanco.head());
dadosBanco.to_sql('clientes', engine, index= False);

inspector = inspect(engine); #variavel para inspecao do banco
#print(inspector.get_table_names()); #pega o nome das tabelas do banco

query = 'SELECT * FROM Clientes WHERE Categoria_de_renda="Empregado"'
empregados = pd.read_sql(query, engine);

print(empregados)
empregados.to_sql ('empregados', con=engine, index=False)
pd.read_sql_table('empregados', engine);
#pd.read_sql_table('empregados', engine, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual'])

query = 'SELECT * FROM Clientes'
pd.read_sql = (query, engine)
query = 'DELETE FROM Clientes WHERE ID_Cliente=5008804';
with engine.connect() as conn:
    conn.execute(query);
query = 'UPDATE Clientes SET Grau+escolaridade="Ensino Superior" WHERE ID_CLiente=5008808'
with engine.connect() as conn:
    conn.execute(query);
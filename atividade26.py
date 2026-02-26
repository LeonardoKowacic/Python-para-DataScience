import pandas as pd;
import numpy as np;
import datetime as dt;

dados = pd.read_json("dados_hospedagem.json");

dados_normalizados = pd.json_normalize(dados['info_moveis'])

colunas = list(dados_normalizados.columns)



dados_explodidos = dados_normalizados.explode(colunas[3:])

index_resetado = dados_explodidos.reset_index(inplace = True, drop = True)

dados_explodidos

colunas_int = ['quantidade_banheiros','quantidade_quartos','quantidade_camas','max_hospedes']

dados_explodidos[colunas_int] = dados_explodidos[colunas_int].astype(np.int64); 

dados_explodidos['avaliacao_geral'] = dados_explodidos['avaliacao_geral'].astype(np.float64)

dados_explodidos[['preco','taxa_limpeza']] = dados_explodidos[['preco','taxa_limpeza']].applymap(lambda x: x.replace('$','').replace(',','').strip());

dados_explodidos[['preco','taxa_limpeza']] = dados_explodidos[['preco','taxa_limpeza']].astype(np.float64)

dados_explodidos['descricao_local'] = dados_explodidos['descricao_local'].str.lower()

dados_explodidos['descricao_local'] = dados_explodidos['descricao_local'].str.replace('[^a-zA-Z0-9\\-\']', ' ', regex=True)

dados_explodidos['descricao_local'] = dados_explodidos['descricao_local'].str.replace('(?<!\w)-(?!\w)', '', regex=True)

dados_explodidos['descricao_local'] = dados_explodidos['descricao_local'].str.split()

dados_explodidos['comodidades'] = dados_explodidos['comodidades'].str.replace('\{|}|\"','',regex=True);

dados_explodidos['comodidades'] = dados_explodidos['comodidades'].str.split()

#print(colunas)
#print(dados_explodidos['preco'])
#print(dados_explodidos.info())
#print(dados_explodidos.head())
#print(dados_explodidos.info())
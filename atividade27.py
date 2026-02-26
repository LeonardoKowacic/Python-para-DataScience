import pandas as pd

emissoes_gases = pd.read_excel('1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name = 'GEE Estados') #sheet_name = puxa apenas a tabela GEE Estados do Excel

#print(emissoes_gases.head());

#print(emissoes_gases.info());

tabela_Emissao = emissoes_gases['Emissão / Remoção / Bunker'].unique(); # retorna um array com cada nome de coluna da tabela

#(emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção') # filtra apenas 'remocao NCI' e 'remocao'

emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção'])] # filtra apenas 'remocao NCI' e 'remocao' utilizando isin() para simplificacao do codigo

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021] # filtra em anos especificos o objetivo e verificar se possuimos apenas valores <= 0

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique() #o objetivo aqui e verificar quais tipos existem dentro da coluna Estado

emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']

emissoes_gases = emissoes_gases.drop(columns = 'Emissão / Remoção / Bunker')

colunas_info = list(emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns)

colunas_emissao = list(emissoes_gases.loc[:,1970:2021].columns)

emissoes_por_ano = emissoes_gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano' , value_name = 'Emissão')

emissoes_por_ano.groupby('Gás')

emissoes_por_ano.groupby('Gás').groups

emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')

emissoes_por_ano.groupby('Gás').sum()

emissao_por_gas = emissoes_por_ano.groupby('Gás').sum().sort_values('Emissão', ascending = False)

#emissao_por_gas.plot(kind = 'barh', figsize = (10,6));

emissao_por_gas.iloc[0:9]

#print(f'A emissão de CO2 corresponde a {float(emissao_por_gas.iloc[0:9].sum()/emissao_por_gas.sum())*100:.2f} % de emissão total de gases estufa no Brasil de 1970 a 2021.')

gas_por_setor = emissoes_por_ano.groupby(['Gás','Nível 1 - Setor'])[['Emissão']].sum()

gas_por_setor.xs('CO2 (t)', level = 0).idxmax()

valores_max = gas_por_setor.groupby(level = 0).max().values

tabela_sumarizada = gas_por_setor.groupby(level = 0).idxmax()

tabela_sumarizada.insert(1, 'Quantidade de emissão',valores_max)

gas_por_setor.swaplevel(0, 1)

gas_por_setor.swaplevel(0, 1).groupby(level = 0).idxmax()\

#emissoes_por_ano.groupby('Ano').mean().plot(figsize = (10,6));

emissoes_por_ano.groupby('Ano').mean().idxmax()

emissoes_por_ano.groupby(['Ano', 'Gás']).mean()

media_emissao_anual = emissoes_por_ano.groupby(['Ano', 'Gás']).mean().reset_index()

media_emissao_anual = media_emissao_anual.pivot_table(index = 'Ano', columns = 'Gás', values = 'Emissão')

#media_emissao_anual.plot(subplots = True, figsize = (10,40));
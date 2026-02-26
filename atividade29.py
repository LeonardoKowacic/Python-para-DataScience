import pandas as pd;
import numpy as np
df = pd.to_csv('relatorio_vendas.csv');

df.info();

df['data_pedido'] = pd.to_datetime(df['data_pedido']);

df_clientes_vendas = df.groupby(['nome_cliente'])['vendas'].sum().nlargest(10).copy() #faz a soma de vendas por cliente e retorna os maiores valores

df_clientes_vendas = df_clientes_vendas.reset_index()

df_clientes_vendas.columns = ['Clientes','Vendas']

df_clientes_vendas['Ranque'] = df_clientes_vendas.index + 1

df_clientes_vendas.set_index('Ranque', inplace = True)

s = df_clientes_vendas.style # transforma a tabela para style

s.format({'Vendas':'R$ {:,.2f}'}) #formata a coluna vendas para R$ (valor) formatado para apenas duas casas decimas 

df_venda_lucro = df.groupby(['tipo_produto'])[['vendas','lucro']].sum()

df_venda_lucro.index.name = 'tipo produto'

estilo_produto = df_venda_lucro.style

estilo_produto.format('R$ {:,.2f}').highlight.max(color = 'green').hightlight.min(color = 'red')

#estilo_produto.format('R$ {:,.2f}').backgorund_gradient(cmap='Greens')

cabecalho = {
    'selector':'th',
    'props': 'font-weight: bold; font-family: Arial; text-align: center; text-transform> capitalize'

}

estilo_produto.set_table_styles([cabecalho], override = False)



df_regiao = pd.DataFrame(df['regiao'])
df_regiao.columns = ['Nº pedidos']


df_regiao.index.name = 'Regiao'
porcentagem = df_regiao['Nº pedidos'].to_numpy() #transforma a coluna n pedidos em um array

porcentagem = df_regiao['Nº pedidos'].to_numpy()
porcentagem = 100 * porcentagem / porcentagem.sum() #calcula a porcentagem e cada item do array

df_regiao['Porcentagem regiao'] = porcentagem

estilo_regiao = df_regiao.style
estilo_regiao

cabecalho = {
    'selector': 'th',
    'props': 'font-weight: bold; font-family: Arial; text-align: right; background-color: white'
}

celulas = {
    'selector': 'td',
    'props': 'background-color: white;'
}

estilo_regiao.set_table_styles([cabecalho,celulas])

estilo_regiao.format({'Porcentagem regiao':'{:.2f} %'})\
             .bar(subset='Porcentagem regiao', vmin=0, vmax=100.0, color='#9CD33B')
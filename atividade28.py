import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns
import plotly.express as px;

url = pd.read_csv('canadian_immegration_data.csv');

sns.set_theme()
sns.set_style()

#print(url.info());

url.set_index('Country', inplace= True);
#print(url.head());
anos = list(map(str, range(1980, 2014)));
america_sul = url.query('Region == "South America"')
america_sul_ordenado = america_sul.sort_values(by='Total')
brasil = url.loc['Brazil', anos];
brasil_dict = {'ano': brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}

dados_brasil = pd.DataFrame(brasil_dict)

#print(dados_brasil)
#plt.figure(figsize=(10,5))
#plt.title('Numero de imigrantes Brasileiros ate 2015', fontsize=18)
#plt.xlabel('anos', fontsize = 12)
#plt.ylabel('imigrantes', fontsize = 12)
#plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
#plt.xticks(['1980','1985','1990','1995','2000','2005','2010','2015'])
#plt.show()

#fig, ax = plt.subplots(figsize=(10, 5));
#ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw =3, marker = 'o', color = 'green');
#ax.set_title('Numero de imigrantes Brasileiros ate 2015', fontsize=18, loc = 'left')
#ax.set_xlabel('anos', fontsize=12)
#ax.set_ylabel('imigrantes', fontsize=12)
#ax.xaxis.set_tick_params(labelsize= 10)
#ax.yaxis.set_tick_params(labelsize= 10)
#ax.xaxis.set_major_locator(plt.MultipleLocator(5));
#plt.grid(linestyle =':')
#ax.spines['top'].set_visible(False)
#ax.spines['right'].set_visible(False)
#fig.savefig('imigracao_brasil_canada.png', transparent=False, dpi=300, bbox_inches='tight')
#plt.show()

cores = []
for pais in america_sul_ordenado.index:
    if pais == "Brazil":
        cores.append('green')
    else:
        cores.append('gray')

#fig, ax = plt.subplots(figsize=(12, 5))
#ax.barh(america_sul_ordenado.index, america_sul_ordenado['Total'], color=cores)
#ax.set_title('Imigração da América do Sul para o Canadá\n1980 a 2013', loc='left', fontsize=18)
#ax.set_ylabel(' ')
#ax.set_xlabel('Número de imigrantes', fontsize=10)
#ax.yaxis.set_tick_params(labelsize=12)
#ax.xaxis.set_tick_params(labelsize=12)
#for i, v in enumerate(america_sul_ordenado['Total']):
#    ax.text(v + 20, i, str(v), color='black', fontsize=10, ha='left', va='center')
#ax.set_frame_on(False)
#ax.get_xaxis().set_visible(False) 
#ax.tick_params(axis='both', which='both', length=0)

#fig.savefig('imigracao_america_sul.png', transparent=False, dpi=300, bbox_inches='tight')    
#plt.show()

top_10 = url.sort_values('Total', ascending=False).head(10)
ax = sns.barplot()
sns.barplot(data=top_10, x = 'Total', y = top_10.index, orient= 'h', palette='Blues_r')
ax.set(title="Países com maior imigração para o Canadá\n1980 a 2013",xlabel='Número de Imigrantes',ylabel = '')

plt.show()

fig = px.line(dados_brasil, x='ano', y= 'imigrantes', title = 'um titulo para meu grafico')

fig.update_traces(line_color = 'blue',line_width = 4)

fig.update_layout(width = 1000, height = 700, xaxis={'tickangle': -45}, font_family = 'Comic Sans MS',
                  font_size = 14, font_color = 'green', title_font_color = 'yellow', title_font_size = 22,
                  xaxis_title = 'Ano', yaxis_title = 'Numero de imigrantes')

fig.show
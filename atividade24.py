import numpy as np
import matplotlib.pyplot as plt;
#carrega a base de dados
dado = np.loadtxt('apples_ts.csv',delimiter= ",", usecols= np.arange(1,88,1));




#dado.ndim mostra as dimensoes do dado 
#dado.size mostra o tamanho do dado
#dado.shape mostra o numero de linhas e colunas desta forma: (linhas, colunas)
dados_transpostos = dado.T #faz a transposicao dos dados

print(dado)

#datas = dados_transpostos[:,0];
datas = np.arange(1,88,1);
precos = dados_transpostos[:,1:6];

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

def anos_um_a_quatro(ano):
    ano1 = ano[0:12]
    ano2 = ano[12:24]
    ano3 = ano[24:36]
    ano4 = ano[36:48]
    plt.plot(np.arange(1,13,1), ano1)
    plt.plot(np.arange(1,13,1), ano2)
    plt.plot(np.arange(1,13,1), ano3)
    plt.plot(np.arange(1,13,1), ano4)
    plt.legend([2013,2014,2015,2016])
    plt.show()
    return ano1, ano2, ano3, ano4 
ano1, ano2, ano3, ano4 = anos_um_a_quatro(Moscow)
np.array_equal(ano1, ano2)
np.allclose(ano1, ano2, 10)
nao_numero = np.isnan(Kaliningrad);
indices = np.where(nao_numero)[0]
#sum(nao_numero);
#for idx in indices:
#    # evita problemas se for o primeiro ou último elemento
#    if 0 < idx < len(Kaliningrad) - 1:
#        np.mean(Kaliningrad[idx - 1] + Kaliningrad[idx + 1]) / 2
#        print(Kaliningrad[idx])
#print(teste)

#fazer uma linha central por tentativa e erro
#y = 2*datas+80;
#
#plt.plot(datas, Moscow);
#plt.plot(datas, y)
#plt.show()
#print(np.linalg.norm(Moscow-y))
#
#y1 = 0.50*datas+80;
#
#plt.plot(datas, Moscow);
#plt.plot(datas, y1)
#plt.show()
#print(np.linalg.norm(Moscow-y1))

tamanho = np.size(Moscow);

formula = (tamanho * np.sum(datas*Moscow) - np.sum(datas) * np.sum(Moscow))/ (tamanho*np.sum(datas**2) - np.sum(datas)**2)

formula2 = np.mean(Moscow) - formula*np.mean(datas)
print(formula)
print(formula2)
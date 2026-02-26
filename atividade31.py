import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import pickle

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

dados = pd.read_csv('/content/marketing_investimento.csv')

dados.info() #caso existam dados nulos devem ser tratados

x = dados.drop('aderencia_investimento', axis = 1)
y = dados['aderencia_investimento']

#px.histogram(dados, x='aderencia_investimento', text_auto = True)

#px.histogram(dados, x= 'estado_civil', text_auto = True, color = 'aderencia_investimento', barmode = 'group')

#px.histogram(dados, x= 'escolaridade', text_auto = True, color = 'aderencia_investimento', barmode = 'group')

#px.histogram(dados, x= 'inadimplencia', text_auto = True, color = 'aderencia_investimento', barmode = 'group')

#px.histogram(dados, x= 'fez_emprestimo', text_auto = True, color = 'aderencia_investimento', barmode = 'group')

#px.box(dados, x = 'idade', color = 'aderencia_investimento')

#px.box(dados, x = 'idade', color = 'aderencia_investimento')

#px.box(dados, x = 'tempo_ult_contato', color = 'aderencia_investimento')

#px.box(dados, x = 'numero_contatos', color = 'aderencia_investimento')

one_hot = make_column_transformer((
    OneHotEncoder(drop = 'if_binary'),
    ['estado_civil', 'escolaridade', 'inadimplencia', 'fez_emprestimo']
),
    remainder = 'passthrough',
    sparse_threshold=0)

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(y)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, stratify = y,  random_state = 5)

arvore = DecisionTreeClassifier(random_state = 5)
arvore.fit(x_treino,y_treino)

arvore.predict(x_teste)

arvore.score(x_teste, y_teste)


nome_colunas = ['casado (a)',
                'divorciado (a)',
                'solteiro (a)',
                'fundamental',
                'medio',
                'superior',
                'inadimplencia',
                'fez_emprestimo',
                'idade',
                'saldo',
                'tempo_ult_contato',
                'numero_contatos']

plt.figure(figsize = (15, 6))
plot_tree(arvore, filled = True, class_names = ['nao', 'sim'], fontsize = 1, feature_names = nome_colunas);

arvore.score(x_treino, y_treino)

arvore = DecisionTreeClassifier(max_depth=3, random_state = 5)
arvore.fit(x_treino,y_treino)

plt.figure(figsize = (15, 6))
plot_tree(arvore, filled = True, class_names = ['nao', 'sim'], fontsize = 1, feature_names = nome_colunas);

normalizacao = MinMaxScaler()

x_treino_normalizado = normalizacao.fit_transform(x_treino)

pd.DataFrame(x_treino_normalizado)

knn = KNeighborsClassifier()

knn.fit(x_treino_normalizado, y_treino)

x_teste_normalizado = normalizacao.transform(x_teste)

with open('modelo_onehotenc.pkl', 'wb') as arquivo:
    pickle.dump(one_hot,arquivo)
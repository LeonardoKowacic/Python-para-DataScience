import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Carregando os dados
uri = "https://gist.githubusercontent.com/guilhermesilveira/b9dd8e4b62b9e22ebcb9c8e89c271de4/raw/c69ec4b708fba03c445397b6a361db4345c83d7a/tracking.csv"
dados = pd.read_csv(uri)

# Definindo x e y
y = dados["comprou"]
x = dados[["inicial", "palestras", "contato", "patrocinio"]]

# Separando dados de treino e teste
treino_x = x[:75]
treino_y = y[:75]
teste_x = x[75:]
teste_y = y[75:]

# Treinando o modelo
modelo = LinearSVC()
modelo.fit(treino_x, treino_y)

# Fazendo previsões
previsoes = modelo.predict(teste_x)

# Calculando a acurácia
acuracia = accuracy_score(teste_y, previsoes) * 100
print(f"A acurácia foi de {acuracia:.2f}%")
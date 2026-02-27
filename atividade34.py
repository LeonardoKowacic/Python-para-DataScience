from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import pandas as pd

uri = "https://gist.githubusercontent.com/guilhermesilveira/b9dd8e4b62b9e22ebcb9c8e89c271de4/raw/c69ec4b708fba03c445397b6a361db4345c83d7a/tracking.csv"
dados = pd.read_csv(uri)


# Separando os dados em treino e teste
y = dados["comprou"]
x = dados[["inicial", "palestras", "contato", "patrocinio"]]
SEED = 4364
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, random_state=SEED, stratify=y)

print(f"Treinaremos com {len(treino_x)} elementos")
print(f"Testaremos com {len(teste_x)} elementos")

# Treinando o modelo
modelo = LinearSVC()
modelo.fit(treino_x, treino_y)

# Fazendo previsões
previsoes = modelo.predict(teste_x)

# Calculando a acurácia
acuracia = accuracy_score(teste_y, previsoes) * 100
print(f"A acurácia foi de {acuracia:.2f}%")

# Verificando a distribuição das classes
print(treino_y.value_counts())
print(teste_y.value_counts())
# features [1 sim, 0 nao]
# pelo longo?
# perna curta?
# faz auau?

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# 1 -> porco, 0 -> cachorro
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
classes = [1, 1, 1, 0, 0, 0]

# Importando o modelo
from sklearn.svm import LinearSVC

modelo = LinearSVC()
modelo.fit(dados, classes)

# Prevendo um animal
animal_misterioso = [0, 1, 1]
previsao = modelo.predict([animal_misterioso])

# Calculando a acurácia da previsão
misterio1 = [1, 1, 1]
misterio2 = [1, 1, 0]
misterio3 = [0, 1, 1]

testes = [misterio1, misterio2, misterio3]
previsoes = modelo.predict(testes)

testes_classes = [0, 1, 1]

# Comparando previsões com classes reais
corretos = (previsoes == testes_classes).sum()
total = len(testes)
taxa_de_acerto = corretos / total * 100

print(f"Acurácia: {taxa_de_acerto:.2f}%")
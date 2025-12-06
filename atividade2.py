gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08];
lista = [];
media = sum(gastos)/len(gastos);

print(media);
gastos3000 = [valor for valor in gastos if valor >= 3000];
percentual = (len(gastos3000) / len(gastos)) * 100
print(percentual)

for i in range(0,5):
    valor = int(input("digite o valor desejado"));
    lista.append(valor);
print(lista);
lista.reverse()
print(lista);
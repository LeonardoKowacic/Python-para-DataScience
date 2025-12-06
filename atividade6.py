ids_doce = [];
ids_amargo = [];

for i in range (1, 11):
    valor = int(input("digite o id do item: "));
    if valor % 2 == 0:
        
        ids_doce.append(valor);
    else:
        ids_amargo.append(valor);

print("tabela de doces: " + str(ids_doce) + "\n" + "tabela de amargos: " + str(ids_amargo))
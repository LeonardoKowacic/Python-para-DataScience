numero_bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9];
aumento_bacterias = [];

for i in range(len(numero_bacterias) - 1):
    
    soma = numero_bacterias[i] + numero_bacterias[i + 1];
    aumento = 100*(numero_bacterias[i+1] - numero_bacterias[i] )/ numero_bacterias[i];
    aumento_arredondado = round(aumento, 2)
    aumento_bacterias.append(aumento_arredondado);
    print(aumento_bacterias);
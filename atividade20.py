import numpy as np
import matplotlib.pyplot as plt
import math
import random 
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

print(random.choice(lista))
print(random.randrange(1, 100));

numero1 = int(input ("digite um numero: "));
numero2 = int(input ("digite um numero: "));

calculo = pow(numero1, numero2)
print(calculo)

pessoas =int(input("digite o numero de pessoas no sorteio"));

print(random.randrange(pessoas));
nome = input("digite seu nome");
tokenUtilizado = [];

while True:
    token = random.randrange(1000, 9999, 2)  
    if token not in tokenUtilizado:          
        tokenUtilizado.append(token)          
        break                                  
print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!");
notas = {'1 trismestre': 8.5, '2 trimestre': 9.5, '3 trismestre': 7};
primeiroTrismestre = notas['1 trismestre'];
segundoTrimestre = notas['2 trimestre'];
terceiroTrimestre = notas['3 trismestre']

soma = primeiroTrismestre + segundoTrimestre + terceiroTrimestre;
somasum = sum(notas.values())
media = soma/len(notas)
print(soma);
print(somasum)
print(f'{media:.2f}')
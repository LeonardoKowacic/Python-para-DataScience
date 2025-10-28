notas = [];

for i in range(0, 3):
    nota = int(input("digite sua nota: "));
    notas.append(nota)

print(notas)

def media (lista):
    calculo = sum(lista) / len(lista)
    return(calculo);

resultado = media(notas);
print(round(resultado,1));
notas = [6.0, 6.0, 6.0, 6.0, 6.0]
qualitativo = 0.5

acrescimo = lambda x: x + qualitativo

novaNota = list(map(acrescimo, notas))  # aplica a função a cada nota
media = sum(novaNota) / len(novaNota)

print(novaNota)
print(media)
notas_turma = ['Joao', 8, 9, 10, 'Maria', 9, 7, 6, 'Jose', 3.5, 7, 7, 'Claudia', 5.5, 6.5, 8.0]
nomes = []
notas1 = []
listas = []
for i in notas_turma:
      if isinstance(i, str):
          nomes.append(i);
      elif isinstance(i, (int, float)):
        notas.append(i);
for i in range(0, len(notas), 3):
    listas.append([notas1[i], notas1[i+1], notas1[i+2]])
#print(listas)
#print(notas)
#print(nomes);
#print(listas[0][1])

from random import randint, sample;

estudantes = ['Joao', 'Maria', 'Jose', 'Claudia']
id = []

def gera_codigo():
    return str(randint(0,999))

for i in range(0, len(estudantes)):
    id.append({estudantes[i] : gera_codigo()});
    
print(id)

for i in listas:
     media = sum(i)/len(i)
     if media < 6:
          print(estudantes[i] + "reprovado");
     else:
          print(estudantes[i] + "aprovado");
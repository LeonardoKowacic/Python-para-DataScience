gabarito = ["D","A","C","B","A","D","C","C","A","B"];
prova_aluno = [];
nota = 0;

for i in gabarito:
   respostas =  input("digite a resposta da questao as alternativas sao de A,B,C ou D: " );
   prova_aluno.append(respostas.upper())

for i in range(len(gabarito)):
    
    if prova_aluno[i] == gabarito[i]:
      nota = nota+1;
      print("sua nota e: "+ str(nota));
import pandas as pd 

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

dados = pd.read_csv(url, sep = ";");

dados = dados.fillna(0);
 
dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio'];

dados['Valor_por_ano'] = dados['Valor_por_mes']*12 + dados['IPTU'];

dados['Descricao'] = dados['Tipo'] +' em ' + dados['Bairro'] + " com " + dados['Quartos'].astype(str) + " quartos e possui " + dados['Vagas'].astype(str) + " vagas de garagem ";
#astype faz com que o dado seja lido como o tipo desejado

dados['Possui_suite'] = dados['Suites'].apply(lambda x: 'sim' if x > 0 else "nao");
# .apply funciona para aplicar um determinada funcao em um conjunto de dados, lambda e um tipo de funcao personalizada que pode ser feito em uma unica linha de codigo

print(dados['Possui_suite'].head(10))

#df.to_csv('dados_completos_dev.csv', index=False, sep = ;)

#Para praticar os métodos aprendidos no decorrer dessa aula e também aprender novos, vamos realizar alguns tratamentos e seleções utilizando um arquivo csv diferente: alunos.csv.
#
#Esse arquivo é o mesmo utilizado para resolução dos desafios da aula 1 e 3 e possui dados referentes a alunos de um curso superior. Com base nisso, solucione os problemas propostos abaixo utilizando os conhecimentos adquiridos até aqui.
#
#1) Os alunos participaram de uma atividade extracurricular e ganharam pontos extras. Esses pontos extras correspondem a 40% da nota atual de cada um deles. Com base nisso, crie uma coluna chamada "Pontos_extras" que contenha os pontos extras de cada aluno, ou seja, 40% da nota atual deles.
#
#2) Crie mais uma coluna, chamada "Notas_finais" que possua as notas de cada aluno somada com os pontos extras.
#
#3) Como houve uma pontuação extra, alguns alunos que não tinham sido aprovados antes podem ter sido aprovados agora. Com base nisso, crie uma coluna chamada "Aprovado_final" com os seguintes valores:
#
#True: caso o aluno esteja aprovado (nota final deve ser maior ou igual a 6);
#False: caso o aluno esteja reprovado (nota final deve ser menor que 6).
#4) Faça uma seleção e verifique quais alunos não tinham sido aprovados anteriormente, mas foram aprovados após a soma dos pontos extras.
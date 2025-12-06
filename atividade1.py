nome = [];
aux = 0;
while aux <= 1:
    loop1 = input("Digite seu nome: ");
    nome.append(loop1);
    print(nome);
    aux = aux+1;
def media():
    numeros = [int(x) for x in nome]
    calculo = sum(numeros) / len(numeros)
    print(calculo)
    
media();

for i in range(0, len(nome[0])): # loop percorre todos os caracteres do primeiro item da lista
    print(nome[0][i]) #printa cada um dos caracteres separadamente

#funcao type(variavel) utilizado para saber qual o tipo da variavel
#variavel.upper() (deixa as letras maiusculas)/ variavel.lower() (deixa as letras minusculas)
#variavel.strip() (retira espacos do comeco e final de uma string)
#variavel.replace(antigo,novo) (substitui todas as ocorrencias do texto "antigo" na string por "novo")

loop1 = loop1.upper().strip().replace("L","G");
print(loop1);
nome[-1] = loop1;
print(nome);
print(type(loop1));
loop1 = int(loop1);
print(type(loop1));
def compara():
    lista = ['José da Silva', 'Maria Oliveira', 'Pedro Martins', 'Ana Souza', 'Carlos Rodrigues', 'Juliana Santos', 'Bruno Gomes', 'Beatriz Costa', 'Felipe Almeida', 'Mariana Fernandes', 'João Pinto', 'Luísa Nascimento', 'Gabriel Souza', 'Manuela Santos', 'Thiago Oliveira', 'Sofia Ferreira', 'Rafael Albuquerque', 'Isabella Gomes', 'Bruno Costa', 'Maria Martins', 'Rafaela Souza', 'Matheus Fernandes', 'Luísa Almeida', 'Beatriz Pinto', 'Mariana Rodrigues', 'Gabriel Nascimento', 'João Ferreira', 'Maria Albuquerque', 'Felipe Oliveira']
    nome_1 = 'Mariana Rodrigues'
    nome_2 = 'Marcelo Nogueira'
    if nome_1 in lista and nome_2 in lista:
        return True
    else:
        lista.append(nome_1);
        lista.append(nome_2);
        print(lista);
        return False    

print(compara())

#and or e not 
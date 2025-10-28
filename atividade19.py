livro = 5;
inicio = 0
fim = 6
for i in range (inicio,fim):
    print(f"Venda realizada! Estoque restante: {livro}");
    livro -=1;
    if i == fim - 1:
        print("estoque esgotado");
regressiva = 10;
for i in range(0,10):
    print(regressiva);
    regressiva -= 1;
    if regressiva == 0:
        print("Aproveite a promoção agora!");
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for i in livros:
    if i ["estoque"] != 0:
     print(f"livro disponivel {i ['nome']}");
i = True;
while i == True:
    user = input("digite seu nome de usuario: ");
    senha = input("digite sua senha: ");
    if len(user)< 5:
        print("o nome de usuario deve ter pelo menos 5 caracteres");
    elif len(senha) < 8:
        print("a senha deve ter pelo menos 8 caracteres");
    else:
        print("cadastro realizado com sucesso!");
        break
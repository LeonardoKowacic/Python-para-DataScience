projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"];

for nome in projetos:
    if nome == str(nome):
        print(nome);
    elif nome == None:
        print("Projeto ausente");
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"];

for i in livros:
     
     if i == "O Hobbit":
       print(f"Livro encontrado: {i}");
       break;

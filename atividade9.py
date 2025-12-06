produtos_vendidos = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
soma_produto = sum(produtos_vendidos.values());
maior_produto = max(produtos_vendidos, key=produtos_vendidos.get);

print (soma_produto);
print (maior_produto + ": " + str(produtos_vendidos[maior_produto]));
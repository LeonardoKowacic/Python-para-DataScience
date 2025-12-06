salarios = {"1172":200 ,"1644":200 ,"2617":260,"5130":513 , "5532":553, "6341":634, "6650":665,"7238":723, "7685":768, "7782":778,"7903":790}
soma_abono = sum(salarios.values());
valor_minimo = 0
for abono in salarios.values():
    
    if abono == 200:
        valor_minimo += 1
maior_abono = max(salarios, key=salarios.get);
print(valor_minimo);
print(maior_abono);

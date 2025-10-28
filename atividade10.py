designs = {"Design1" : 1334, "Design2" : 982,  "Design3" : 1751, "Design4" : 210,  "Design5" : 1811};

design_vencedor = max(designs, key=designs.get);
soma_desing = sum(designs.values());
porcentagem_votos = (designs[design_vencedor]/soma_desing)*100;

print(design_vencedor);
print(f"Isto representa {porcentagem_votos:.2f}% do total de votos.")
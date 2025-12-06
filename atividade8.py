temperatura_ano = [];
temperaturas_acima = [];
mes = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
for i in range(0,12):
    temperatura = int(input("digite a media de temperatura do mes:"));
    temperatura_ano.append(temperatura);

media_ano = sum(temperatura_ano)/len(temperatura_ano);
print(media_ano);
for i in range(len(temperatura_ano)):
    
    if temperatura_ano[i] > media_ano:
        temperaturas_acima.append(temperatura_ano[i])
        print(f"{mes[i]} está acima da média: {temperatura_ano[i]}°C")
print(str(temperatura_ano));
print(str(temperaturas_acima));
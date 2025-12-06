data = input("digite a data desejada no seguinte molde dd/mm/aaaa: ");
partes = data.split("/");
dia = int(partes[0]);
mes = int(partes[1]);
ano = partes[2];
if dia > 31:
    
    print("essa nao e uma data valida");
elif mes > 12:
    print("essa nao e uma data valida");
elif len(ano) != 4:
    print("essa nao e uma data valida");
else:
    print("essa e uma data valida! "+ data);
# dd <= 31 mm <= 12 
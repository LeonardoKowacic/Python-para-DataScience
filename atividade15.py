altura = float(input("digite sua altura: "));
peso = float(input("digite seu peso atual: "));
IMC = peso/(altura**2);
print(f"Seu IMC é: {IMC:.2f}")
if IMC < 18.5:
    print("voce esta abaixo do peso");

elif IMC >= 18.15 and IMC < 25:
    print("voce esta com o peso normal")

elif IMC > 25:
    print("voce esta acima do peso normal")
    
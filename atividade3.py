def gerar_primos():
    numero = int(input("Digite o número máximo: "))
    primos = []


    for n in range(2, numero + 1):
        primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                primo = False
                break
        if primo:
            primos.append(n)

    print(f"Números primos até {numero}: {primos}")
    return primos

gerar_primos()
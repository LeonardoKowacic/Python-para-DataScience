i = True;
while i == True:

    A = float(input("informe dias para a atividade A: "));
    B = float(input("informe dias para a atividade B: "));
    C = float(input("informe dias para a atividade C: "));
    if A < 0 or B < 0 or C < 0:

        print ("erro: Os dias nao podem ser negativos");
    else:
        
        math = A + B + C;
        print("o numero de dias necessario e: "+ str(math));
        break;
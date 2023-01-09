while True:
    try:
        n1 = float(input("Informe o primeiro numero: "))
        n2 = float(input("Informe o segundo numero: "))
        sinal = input("Informe a operação +(mais) -(menos) *(multiplicação) ou /(divisão): ")

        if sinal == '+':
            print(n1+n2)

        elif sinal == '-':
            print(n1-n2)

        elif sinal == '*':
            print(n1*n2)

        elif sinal == '/':
            print(n1/n2)

        else:
            print("O sinal não é reconhecido")
    except:

            print("O valor informado não é um número")
            continue
        
    
    #condição de parada
    sair = input("Deseja sair? [s]im: ").lower().startswith('s')
    if sair is True:
        break

import os
import time

def verifica_primeiro_digito(cpf):
    cpf_particionado = ''
    cpf_multiplicado = 0
    cpf_resto = 0
    flag_cpf = 10
    cpf_com_digito = ''

    for i in cpf:

        if i == '.':
            continue
        elif i == '-':
            break

        else:
            cpf_particionado += i

    for i in range(len(cpf_particionado)):
        indice_cpf_int = int(cpf_particionado[i])
        cpf_multiplicado += (indice_cpf_int*flag_cpf)
        flag_cpf -= 1
        

    cpf_resto = (cpf_multiplicado * 10)% 11

    if cpf_resto > 9:
        cpf_resto = 0

    
    cpf_resto = str(cpf_resto)
    cpf_com_digito = cpf_particionado + cpf_resto

    return(cpf_com_digito)

def verifica_segundo_digito(cpf):
    cpf_particionado = cpf
    cpf_multiplicado = 0
    cpf_resto = 0
    flag_cpf = 11

    for i in range(len(cpf_particionado)):
        indice_cpf_int = int(cpf_particionado[i])
        cpf_multiplicado += (indice_cpf_int*flag_cpf)
        flag_cpf -= 1
        

    cpf_resto = (cpf_multiplicado * 10)% 11

    if cpf_resto > 9:
        cpf_resto = 0

    
    primeiro_segundo_digito = cpf_particionado[-1] + str(cpf_resto)

    return primeiro_segundo_digito

def valida_cpf(cpf):
    
    try:
        cpf_com_primeiro_digito = verifica_primeiro_digito(cpf)
        cpf_com_segundo_digito = verifica_segundo_digito(cpf_com_primeiro_digito)

        if cpf_com_segundo_digito == (cpf[-2] + cpf[-1]):
            os.system('clear')
            print(f"CPF: {cpf[0:3]}.{cpf[4:7]}.{cpf[8:11]}-{cpf[12:]} é válido")
            time.sleep(4)

        else:
            os.system('clear')
            print(f'CPF: {cpf[0:3]}.{cpf[4:7]}.{cpf[8:11]}-{cpf[12:]} não é válido')
            time.sleep(4)

    except Exception as error:
        print(error)
        time.sleep(3)
        os.system('clear')
        print("Ocorreu um erro, verifique se sua formatação está correta!")

def menu():
    print('Validador de CPF')
    print('1- Validar CPF\n2- Sair')
    print('Digite uma opção: ', end='')
    

while True:
    
    menu()
    entrada = input()
    if entrada == '1':
        os.system('clear')
        cpf = (input("Informe o CPF com a formatação: xxx.xxx.xxx-xx\n"))
        cpf_formatado = cpf.replace('.', '').replace('-', '')
        if cpf_formatado == cpf[0]*len(cpf_formatado):
            print('Informe um CPF válido com números não repetidos')
            time.sleep(2)
            os.system('clear')
        else:
            valida_cpf(cpf)
        
    elif entrada == '2':
        break
    else:
        print('Valor incorreto, tente novamente!')
        time.sleep(4)
        os.system('clear')

    

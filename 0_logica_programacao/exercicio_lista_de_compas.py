from os import system
import os
import time


lista = []
while True:
    print('Escolha uma opção:')
    entrada = (input('(i)-Inserir \n(r)-Remover \n(l)-Listar \n(s)-Sair \n').lower())
    if entrada == 'i':
        valor = input('Insira um valor: ')
        lista.append(valor)
        print('Valor inserido!')
        time.sleep(1)
        os.system('clear')

    elif entrada == 'r':
        try:
            indice = int(input('Informe o indice: '))
            lista.pop(indice)
            os.system('clear')

        except Exception as error:
            print(error)
            time.sleep(3)
            os.system('clear')
            print('Voltando ao menu...')
            time.sleep(2)
            continue
        

    elif entrada == 'l':
        if len(lista) > 0:
            os.system('clear')
            for indice, valor in enumerate(lista):
                print(f'Indice:{indice}, Valor: {valor}')
            time.sleep(1)
                
            
        else:
            print('A lista está vazia!')
            time.sleep(1)
            os.system('clear')
            continue

    elif entrada == 's':
        os.system('clear')
        print('Saindo...')
        time.sleep(2)
        break

    else:
        os.system('clear')
        print('Valor digitado incorreto')
        time.sleep(1)
        continue

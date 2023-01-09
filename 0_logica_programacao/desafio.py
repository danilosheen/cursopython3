print("Informe o nome: ", end='')
nome = input()
print("Informe o idade: ", end='')
idade = int(input())
print("Informe o altura: ", end='')
altura = float(input())
print("Informe o peso:", end='')
peso = float(input())
print('')
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso/altura**2
print(f'{nome} tem {idade} anos, {altura:.1f} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')
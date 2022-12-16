# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#criando a lógica da solução manual
# lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista2 = ['BA', 'SP', 'MG', 'RJ']

# def zipper(lista1, lista2):
#     return [
#         (lista1[i], lista2[i])
#         for i in range(min(len(lista1), len(lista2)))
#     ]
    
# print(zipper(lista1, lista2))

#usando o zip do python
from itertools import zip_longest

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(lista1, lista2)))
print(list(zip_longest(lista1, lista2, fillvalue='Valor Vazio')))
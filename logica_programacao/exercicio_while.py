nome= 'Cicero Danilo'
nome_alterado = ''
tamanho_string = len(nome)
contador = 0
while contador < tamanho_string:
    letra = nome[contador]
    nome_alterado += '*{}'.format(letra)
    contador += 1

print(nome_alterado)
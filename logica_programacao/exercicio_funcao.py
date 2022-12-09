def multiplica(*args):
    valor_multiplicado = 1
    for i in args:
        if i == 0:
            return 0

        valor_multiplicado *= i

    return valor_multiplicado

valor = multiplica(1,2,3,4,5)
print(valor)

def impar_par(numero):
    if numero % 2 == 0: 
        return (f'O número {numero} é par')

    return (f'O número {numero} é ímpar')

print(impar_par(2))
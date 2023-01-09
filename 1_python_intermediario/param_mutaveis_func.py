#se o parâmetro for mutável, não adicionar valor padrão use o None 
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
        
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('João')
adiciona_clientes('Maria', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Fernando')
adiciona_clientes('Francisco', cliente2)
print(cliente2)
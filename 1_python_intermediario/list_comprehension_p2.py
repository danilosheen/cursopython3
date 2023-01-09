#lista com tuplas em for encadeado
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
        
#lista com tuplas em for encadeado usando comprehension
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)
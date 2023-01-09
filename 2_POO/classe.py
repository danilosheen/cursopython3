class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome




p1 = Pessoa('Cicero', 'Danilo')

p2 = Pessoa('Vilma', 'Ferreira')

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)
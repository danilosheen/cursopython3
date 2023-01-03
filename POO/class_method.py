# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    
    @classmethod
    def criar_com_50(cls, nome):
        return cls(nome, 50)
        
    
    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônimo', idade)
        
p1 = Pessoa('João', 20)
p2 = Pessoa.criar_com_50('Helena')
p3 = Pessoa.criar_anonimo(34)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
# print(Pessoa.ano)
Pessoa.metodo_de_classe()
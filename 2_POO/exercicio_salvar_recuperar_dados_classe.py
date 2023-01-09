# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = './POO/exercicio_JSON.json'

class Pessoa:
    
    def __init__(self, nome, data_nascimento, altura, peso):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.altura = altura
        self.peso = peso
        
p1 = Pessoa('Danilo', '20/05/1999', 1.78, 82.00)
p2 = Pessoa('Joaquim', '20/05/2000', 1.79, 82.00)
p3 = Pessoa('Fernando', '20/05/2001', 1.80, 82.00)

bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)

print(bd)

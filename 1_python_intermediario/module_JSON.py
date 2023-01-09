#importando modulo json
import json

#dicionario pessoa
pessoa = {
    'nome': 'Cicero Danilo',
    'sobrenome': 'Ferreira da Silva',
    'endereços': [
        {'rua': 'Rua 1', 'numero': 1000},
        {'rua': 'Rua 2', 'numero': 2000},
    ],
    'altura': 1.75,
    'numeros_preferidos': (3, 5, 7, 13, 99),
    'dev': True,
    'nada': None,
}

#converte pessoa em JSON
with open('pessoa.json', 'w', encoding='utf8') as pessoa_json_arquivo:
    json.dump(
        pessoa, pessoa_json_arquivo,
        ensure_ascii=False,
        indent=2
        
    )
    
#converte JSON em pessoa
with open('pessoa.json', 'r', encoding='utf8') as arquivo:
    pessoa_convert = json.load(arquivo)
    print(pessoa_convert)
